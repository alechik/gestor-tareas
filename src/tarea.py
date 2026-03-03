"""
Clase Tarea.
"""

class Tarea:
    def __init__(self, id, descripcion, completada=False):
        """
        Constructor:

        id: Identificador único de la tarea
        descripcion: Descripción de la tarea
        completada: Estado de la tarea (true completado)
        """
        self.id = id
        self.descripcion = descripcion
        self.completada = completada

    def marcar_completada(self):
        """
        Marca la tarea como completada.
        """
        self.completada = True

    def __str__(self):
        """
        Muestra la tarea en consola.
        """
        estado = "✔" if self.completada else "✘"
        return f"[{estado}] ({self.id}) {self.descripcion}"