import os
from datetime import datetime

tareas = []
id_counter = 1

# Funciones auxiliares
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_fecha_actual():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def validar_prioridad(prioridad):
    return prioridad in ['Alta', 'Media', 'Baja']

#Menu Principal
def mostrar_menu():
    limpiar_pantalla()
    print("=== GESTOR DE TAREAS PERSONALES ===")
    print("1. Agregar nueva tarea")
    print("2. Ver todas las tareas")
    print("3. Ver solo tareas pendientes")
    print("4. Ver solo tareas completadas")
    print("5. Marcar tarea como completada")
    print("6. Editar tarea")
    print("7. Eliminar tarea")
    print("8. Buscar tareas")
    print("9. Salir del programa")

#Funciones de gestion de tareas
def agregar_tarea():
    global id_counter
    print("\n--- AGREGAR NUEVA TAREA ---")
    titulo = input("Título de la tarea: ").strip()
    if not titulo:
        print("Error: El título no puede estar vacío.")
        input("Presiona Enter para continuar...")
        return

    descripcion = input("Descripción (Opcional): ").strip()
    while True:
        prioridad = input("Prioridad (Alta/Media/Baja): ").strip().capitalize()
        if validar_prioridad(prioridad):
            break
        print("Error: Prioridad inválida. Usa Alta, Media o Baja.")

    fecha_limite = input("Fecha límite (YYYY-MM-DD) o dejar vacío: ").strip()
    if not fecha_limite:
        fecha_limite = "Sin límite"

    nueva_tarea = {
        'id': id_counter,
        'titulo': titulo,
        'descripcion': descripcion,
        'prioridad': prioridad,
        'estado': 'Pendiente',
        'fecha_creacion': obtener_fecha_actual(),
        'fecha_limite': fecha_limite
    }

    tareas.append(nueva_tarea)
    id_counter += 1
    print(f"\n Tarea #{nueva_tarea['id']} agregada correctamente.")
    input("Presiona Enter para continuar...")

def mostrar_lista(lista_tareas, titulo_filtro="TAREAS"):

    limpiar_pantalla()
    print(f"\n--- {titulo_filtro} ---")
    
    if not lista_tareas:
        print("No hay tareas registradas.")
    else:
        print(f"{'ID':<5} {'TÍTULO':<25} {'PRIORIDAD':<10} {'ESTADO':<12} {'LÍMITE':<15}")
        print("-" * 70)
        for tarea in lista_tareas:
            print(f"{tarea['id']:<5} {tarea['titulo']:<25} {tarea['prioridad']:<10} {tarea['estado']:<12} {tarea['fecha_limite']:<15}")
    print("-" * 70)
    input("Presiona Enter para continuar...")

def ver_todas():
    mostrar_lista(tareas, "LISTA COMPLETA DE TAREAS")

def ver_pendientes():
    pendientes = [t for t in tareas if t['estado'] == 'Pendiente']
    mostrar_lista(pendientes, "TAREAS PENDIENTES")

def ver_completadas():
    completadas = [t for t in tareas if t['estado'] == 'Completada']
    mostrar_lista(completadas, "TAREAS COMPLETADAS")

def marcar_completada():
    if not tareas:
        print("No hay tareas para marcar.")
        input("Enter...")
        return

    mostrar_lista(tareas, "TAREAS")
    try:
        id_tarea = int(input("Ingresa el ID de la tarea a completar: "))
        tarea = next((t for t in tareas if t['id'] == id_tarea), None)
        
        if tarea:
            if tarea['estado'] == 'Completada':
                print("Esta tarea ya está completada.")
            else:
                tarea['estado'] = 'Completada'
                print(f"Tarea #{id_tarea} marcada como completada.")
        else:
            print("Error: ID de tarea no encontrado.")
    except ValueError:
        print("Error: Ingresa un número válido.")
    input("Enter...")

def editar_tarea():
    if not tareas:
        print("No hay tareas para editar.")
        input("Enter...")
        return

    mostrar_lista(tareas, "TAREAS")
    try:
        id_tarea = int(input("Ingresa el ID de la tarea a editar: "))
        tarea = next((t for t in tareas if t['id'] == id_tarea), None)
        
        if tarea:
            print(f"\nEditando tarea: {tarea['titulo']}")
            
            nuevo_titulo = input("Nuevo título (dejar vacío para mantener): ").strip()
            if nuevo_titulo:
                tarea['titulo'] = nuevo_titulo

            nueva_desc = input("Nueva descripción (dejar vacío para mantener): ").strip()
            if nueva_desc:
                tarea['descripcion'] = nueva_desc

            nueva_prioridad = input("Nueva prioridad (Alta/Media/Baja) o vacío: ").strip().capitalize()
            if nueva_prioridad and validar_prioridad(nueva_prioridad):
                tarea['prioridad'] = nueva_prioridad

            nueva_limite = input("Nueva fecha límite (YYYY-MM-DD) o vacío: ").strip()
            if nueva_limite:
                tarea['fecha_limite'] = nueva_limite

            print("Tarea actualizada.")
        else:
            print("Error: ID de tarea no encontrado.")
    except ValueError:
        print("Error: Ingresa un número válido.")
    input("Enter...")

def eliminar_tarea():
    if not tareas:
        print("No hay tareas para eliminar.")
        input("Enter...")
        return

    mostrar_lista(tareas, "TAREAS")
    try:
        id_tarea = int(input("Ingresa el ID de la tarea a eliminar: "))
        tarea = next((t for t in tareas if t['id'] == id_tarea), None)
        
        if tarea:
            confirmacion = input(f"¿Estás seguro de eliminar '{tarea['titulo']}'? (s/n): ").lower()
            if confirmacion == 's':
                tareas.remove(tarea)
                print("Tarea eliminada.")
            else:
                print("Eliminación cancelada.")
        else:
            print("Error: ID de tarea no encontrado.")
    except ValueError:
        print("Error: Ingresa un número válido.")
    input("Enter...")

def buscar_tareas():
    if not tareas:
        print("No hay tareas para buscar.")
        input("Enter...")
        return

    print("\n--- BÚSQUEDA ---")
    palabra_clave = input("Ingresa palabra clave (Título o Descripción): ").lower()
    
    resultados = [t for t in tareas if palabra_clave in t['titulo'].lower() or palabra_clave in t['descripcion'].lower()]
    
    if resultados:
        print(f"\n Se encontraron {len(resultados)} resultado(s) encontrado(s):")
        for tarea in resultados:
            print(f"ID: {tarea['id']} | Título: {tarea['titulo']} | Estado: {tarea['estado']}")
    else:
        print("No se encontraron tareas con esa búsqueda.")
    input("Enter...")

# Funcion Principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_todas()
        elif opcion == "3":
            ver_pendientes()
        elif opcion == "4":
            ver_completadas()
        elif opcion == "5":
            marcar_completada()
        elif opcion == "6":
            editar_tarea()
        elif opcion == "7":
            eliminar_tarea()
        elif opcion == "8":
            buscar_tareas()
        elif opcion == "9":
            print("ADIOS Hasta Luego")
            break
        else:
            print("Opción no válida.")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()