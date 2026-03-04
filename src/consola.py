"""
Interfaz de consola.
"""

from src.gestor import GestorTareas
from src.archivo import ArchivoTareas


class ConsolaTareas:
    def __init__(self):
        """
        Inicializa
        """
        self.gestor = GestorTareas()
        self.archivo = ArchivoTareas("data/tareas.txt")
        self.cargar_datos()

    def cargar_datos(self):
        """
        Carga tareas del archivo al iniciar la aplicación.
        """
        tareas = self.archivo.cargar()
        self.gestor.tareas = tareas
        if tareas:
            self.gestor.siguiente_id = max(t.id for t in tareas) + 1

    def mostrar_menu(self):
        """
        Muestra menú principal.
        """
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Marcar tarea como completada")
        print("4. Listar tareas pendientes")
        print("5. Salir")

    def ejecutar(self):
        """
        Bucle de la aplicación.
        """
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                descripcion = input("Ingrese la descripción de la tarea: ")
                tarea = self.gestor.agregar_tarea(descripcion)
                print(f"Tarea agregada: {tarea}")

            elif opcion == "2":
                try:
                    id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
                    if self.gestor.eliminar_tarea(id_tarea):
                        print("Tarea eliminada correctamente.")
                    else:
                        print("No se encontró la tarea.")
                except ValueError:
                    print("ID inválido. Debe ingresar un número.")

            elif opcion == "3":
                try:
                    id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
                    if self.gestor.marcar_completada(id_tarea):
                        print("Tarea marcada como completada.")
                    else:
                        print("No se encontró la tarea.")
                except ValueError:
                    print("ID inválido. Debe ingresar un número.")

            elif opcion == "4":
                pendientes = self.gestor.listar_pendientes()
                if not pendientes:
                    print("No hay tareas pendientes.")
                else:
                    for tarea in pendientes:
                        print(tarea)

            elif opcion == "5":
                self.archivo.guardar(self.gestor.tareas)
                print("Tareas guardadas. Saliendo...")
                break

            else:
                print("Opción no válida. Intente nuevamente.")