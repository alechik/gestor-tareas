"""
Clase que centraliza y gestiona la lógica del sistema.
"""

from src.tarea import Tarea

class GestorTareas:
    def __init__(self):
        """
        Constructor:
        Inicializa una lista vacía y un contador de IDs.
        """
        self.tareas = []
        self.siguiente_id = 1

    def agregar_tarea(self, descripcion):
        """
        Agrega una tarea al gestor.

        descripcion: Texto descriptivo de la tarea
        return: La tarea creada
        """
        tarea = Tarea(self.siguiente_id, descripcion)
        self.tareas.append(tarea)
        self.siguiente_id += 1
        return tarea

    def eliminar_tarea(self, id_tarea):
        """
        Elimina una tarea por ID.

        id_tarea: ID de la tarea a eliminar
        return: True si se eliminó, False si no se encontró
        """
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                self.tareas.remove(tarea)
                return True
        return False

    def marcar_completada(self, id_tarea):
        """
        Marca una tarea como completada.

        id_tarea: ID de la tarea
        return: True si se marcó, False si no se encontró
        """
        tarea = self.obtener_tarea_por_id(id_tarea)
        if tarea:
            tarea.marcar_completada()
            return True
        return False

    def listar_pendientes(self):
        """
        Devuelve una lista de tareas no completadas.
        """
        return [tarea for tarea in self.tareas if not tarea.completada]

    def obtener_tarea_por_id(self, id_tarea):
        """
        Busca una tarea por ID.

        id_tarea: ID de la tarea
        return: La tarea si existe, None si no
        """
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                return tarea
        return None