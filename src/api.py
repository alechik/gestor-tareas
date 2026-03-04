from flask import Flask, jsonify, request
from src.gestor import GestorTareas
from src.archivo import ArchivoTareas

app = Flask(__name__)

# Usamos la misma ruta de archivo que la consola
archivo = ArchivoTareas("data/tareas.txt")
gestor = GestorTareas()

# Cargar tareas al iniciar la API (igual que la consola)
_tareas_iniciales = archivo.cargar()
gestor.tareas = _tareas_iniciales
if _tareas_iniciales:
    gestor.siguiente_id = max(t.id for t in _tareas_iniciales) + 1


@app.route("/", methods=["GET"])
def index():
    """
    Ruta raíz informativa.
    """
    return jsonify({
        "mensaje": "API Gestor de Tareas activa",
        "endpoints": {
            "GET /tareas": "Listar todas las tareas",
            "POST /tareas": "Crear una nueva tarea",
            "GET /tareas/<id>": "Obtener tarea por ID",
            "PUT /tareas/<id>": "Marcar tarea como completada",
            "DELETE /tareas/<id>": "Eliminar tarea"
        }
    })


@app.route("/tareas", methods=["GET", "POST"])
def tareas():
    """
    GET: Listar todas las tareas
    POST: Crear una nueva tarea
    """
    if request.method == "GET":
        return jsonify(gestor.listar_tareas())

    if request.method == "POST":
        data = request.get_json()

        if not data or "descripcion" not in data:
            return jsonify({"error": "Campo 'descripcion' requerido"}), 400

        descripcion = data["descripcion"].strip()
        if not descripcion:
            return jsonify({"error": "La descripción no puede estar vacía"}), 400

        tarea = gestor.agregar_tarea(descripcion)
        archivo.guardar(gestor.tareas)

        return jsonify({
            "id": tarea.id,
            "descripcion": tarea.descripcion,
            "completada": tarea.completada
        }), 201


@app.route("/tareas/<int:id_tarea>", methods=["GET"])
def obtener_tarea(id_tarea):
    """
    Devuelve una tarea específica por ID.
    """
    for tarea in gestor.tareas:
        if tarea.id == id_tarea:
            return jsonify({
                "id": tarea.id,
                "descripcion": tarea.descripcion,
                "completada": tarea.completada
            })

    return jsonify({"error": "Tarea no encontrada"}), 404

@app.route("/tareas/<int:id_tarea>", methods=["PUT"])
def completar_tarea(id_tarea):
    """
    Marca una tarea como completada.
    """
    if gestor.marcar_completada(id_tarea):
        archivo.guardar(gestor.tareas)

        for tarea in gestor.tareas:
            if tarea.id == id_tarea:
                return jsonify({
                    "id": tarea.id,
                    "descripcion": tarea.descripcion,
                    "completada": tarea.completada
                })

    return jsonify({"error": "Tarea no encontrada"}), 404

@app.route("/tareas/<int:id_tarea>", methods=["DELETE"])
def eliminar_tarea(id_tarea):
    """
    Elimina una tarea por ID.
    """
    if gestor.eliminar_tarea(id_tarea):
        archivo.guardar(gestor.tareas)
        return jsonify({"mensaje": "Tarea eliminada correctamente"})

    return jsonify({"error": "Tarea no encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)