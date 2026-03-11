import os
tareas = []

#Creación visual del menú principal
def mostrar_menu():
    print("\n---- GESTOR DE TAREAS ----")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Actualizar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("--------------------------")

#Función agregar tarea
def agregar_tarea():
    descripcion = input("Escribe la nueva tarea: ")
    
    if descripcion:
        tarea = {
            'descripcion': descripcion,
            'completada': False
        }
        tareas.append(tarea)
        print(f"Tarea '{descripcion}' agregada correctamente.")
    else:
        print("Error: La descripción no puede estar vacía.")
    input("Presiona Enter para continuar...")

#Función para visualizar tareas
def leer_tareas():
    print("\n--- LISTA DE TAREAS ---")
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        for i, tarea in enumerate(tareas, 1):
            estado = "Completada" if tarea['completada'] else "Pendiente"
            print(f"{i}. [{estado}] {tarea['descripcion']}")
    print("-" * 30)
    input("Presiona Enter para continuar...")

#Función para actualizar la tarea
def actualizar_tarea():
    if not tareas:
        print("No hay tareas para actualizar.")
        input("Presiona Enter para continuar...")
        return

    leer_tareas()
    try:
        indice = int(input("Número de tarea a actualizar: ")) - 1
        
        if 0 <= indice < len(tareas):
            tarea = tareas[indice]
            nueva_descripcion = input("Nueva descripción (dejar vacío para no cambiar): ")
            nuevo_estado = input("Nuevo estado (1=Completada, 0=Pendiente, dejar vacío para no cambiar): ")
            
            if nueva_descripcion:
                tarea['descripcion'] = nueva_descripcion
            if nuevo_estado:
                tarea['completada'] = (nuevo_estado == "1")
            
            print("Tarea #" + str(indice + 1) + " actualizada.")
        else:
            print("Error: Índice inválido.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")
    input("Presiona Enter para continuar...")

#Función eliminar tarea
def eliminar_tarea():
    if not tareas:
        print("No hay tareas para eliminar.")
        input("Presiona Enter para continuar...")
        return

    leer_tareas()
    try:
        indice = int(input("Número de tarea a eliminar: ")) - 1
        
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print("Tarea '" + tarea_eliminada['descripcion'] + "' eliminada.")
        else:
            print("Error: Índice inválido.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")
    input("Presiona Enter para continuar...")

#Función principal (Bucle del programa)
def main():
    while True:
        os.system("clear")  # Limpia pantalla (en Windows usa "cls")
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            leer_tareas()
        elif opcion == "2":
            agregar_tarea()
        elif opcion == "3":
            actualizar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("ADIOS")
            break
        else:
            print("Opción no válida.")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()