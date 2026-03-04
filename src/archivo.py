"""
Clase encargada guardar tareas en un archivo de texto.
"""

from src.tarea import Tarea


class ArchivoTareas:
    def __init__(self, ruta_archivo):
        """
        Constructor:

        ruta_archivo: Ruta del archivo donde se guardan las tareas
        """
        self.ruta_archivo = ruta_archivo

    def guardar(self, tareas):
        """
        Guarda la lista de tareas en el archivo.

        tareas: Lista de objetos tarea
        """
        with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
            for tarea in tareas:
                linea = f"{tarea.id}|{tarea.descripcion}|{int(tarea.completada)}\n"
                archivo.write(linea)

    def cargar(self):
        """
        Carga tareas desde el archivo.

        return: Lista de objetos Tarea
        """
        tareas = []

        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if not linea:
                        continue

                    id_tarea, descripcion, completada = linea.split("|")
                    tarea = Tarea(
                        int(id_tarea),
                        descripcion,
                        bool(int(completada))
                    )
                    tareas.append(tarea)
        except FileNotFoundError:
            # Si el archivo no existe, simplemente se devuelve una lista vacía
            pass

        return tareas