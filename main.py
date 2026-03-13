"""
GESTOR DE TAREAS PERSONALES

Un sistema de línea de comandos para gestionar tareas personales con
características de priorización, fechas límite y seguimiento de estado.

Autor: Anthony Vite - Emily Alvarez
"""

import os
from datetime import datetime

#ESTRUCTURA DE DATOS
tareas = []  # Lista global para almacenar todas las tareas
id_counter = 1  # Contador para generar IDs únicos secuenciales

#FUNCIONES AUXILIARES

def limpiar_pantalla():
    """
    Limpia la pantalla de la consola según el sistema operativo.
    Returns:
        None
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_fecha_actual():
    """
    Obtiene la fecha y hora actual formateada.
    Returns:
        str: Fecha y hora actual en formato 'YYYY-MM-DD HH:MM'
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def validar_prioridad(prioridad):
    """
    Valida que la prioridad sea una opción válida.
    Args:
        prioridad (str): La prioridad a validar ('Alta', 'Media', 'Baja')
    Returns:
        bool: True si la prioridad es válida, False en caso contrario
    """
    return prioridad in ['Alta', 'Media', 'Baja']

#MENÚ PRINCIPAL

def mostrar_menu():
    """
    Muestra el menú principal de opciones del programa.
    Returns:
        None
    """
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

#FUNCIONES DE GESTIÓN DE TAREAS

def agregar_tarea():
    """
    Agrega una nueva tarea a la lista de tareas.
    
    Solicita al usuario el título, descripción, prioridad y fecha límite.
    Valida que el título no esté vacío y que la prioridad sea válida.
    Returns:
        None
    """
    global id_counter
    print("\n--- AGREGAR NUEVA TAREA ---")
    
    #Validación Título
    titulo = input("Título de la tarea: ").strip()
    if not titulo:
        print("Error: El título no puede estar vacío.")
        input("Presiona Enter para continuar...")
        return

    descripcion = input("Descripción (Opcional): ").strip()
    
    #Validación Prioridad
    while True:
        prioridad = input("Prioridad (Alta/Media/Baja): ").strip().capitalize()
        if validar_prioridad(prioridad):
            break
        print("Error: Prioridad inválida. Usa Alta, Media o Baja.")

    #Fecha Límite
    fecha_limite = input("Fecha límite (YYYY-MM-DD) o dejar vacío: ").strip()
    if not fecha_limite:
        fecha_limite = "Sin límite"

    #Crear diccionario de tarea
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
    """
    Muestra una lista de tareas con formato de tabla.
    
    Args:
        lista_tareas (list): Lista de diccionarios de tareas a mostrar
        titulo_filtro (str): Título del encabezado de la lista
    Returns:
        None
    """
    limpiar_pantalla()
    print(f"\n--- {titulo_filtro} ---")
    
    if not lista_tareas:
        print("No hay tareas registradas.")
    else:
        # Encabezados de la tabla
        print(f"{'ID':<5} {'TÍTULO':<25} {'PRIORIDAD':<10} {'ESTADO':<12} {'LÍMITE':<15}")
        print("-" * 70)
        for tarea in lista_tareas:
            print(f"{tarea['id']:<5} {tarea['titulo']:<25} {tarea['prioridad']:<10} {tarea['estado']:<12} {tarea['fecha_limite']:<15}")
    print("-" * 70)
    input("Presiona Enter para continuar...")

def ver_todas():
    """
    Muestra todas las tareas registradas en el sistema.
    Returns:
        None
    """
    mostrar_lista(tareas, "LISTA COMPLETA DE TAREAS")

def ver_pendientes():
    """
    Muestra solo las tareas con estado 'Pendiente'.
    Filtra la lista global de tareas y muestra únicamente las pendientes.
    Returns:
        None
    """
    pendientes = [t for t in tareas if t['estado'] == 'Pendiente']
    mostrar_lista(pendientes, "TAREAS PENDIENTES")

def ver_completadas():
    """
    Muestra solo las tareas con estado 'Completada'.
    Filtra la lista global de tareas y muestra únicamente las completadas.
    Returns:
        None
    """
    completadas = [t for t in tareas if t['estado'] == 'Completada']
    mostrar_lista(completadas, "TAREAS COMPLETADAS")

def marcar_completada():
    """
    Marca una tarea específica como completada.
    Solicita al usuario el ID de la tarea a completar y actualiza su estado.
    Returns:
        None
    """
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
    """
    Edita una tarea existente en el sistema.
    
    Permite modificar título, descripción, prioridad y fecha límite.
    Los campos vacíos mantienen su valor original.
    Returns:
        None
    """
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
            
            # Editar Título
            nuevo_titulo = input("Nuevo título (dejar vacío para mantener): ").strip()
            if nuevo_titulo:
                tarea['titulo'] = nuevo_titulo

            # Editar Descripción
            nueva_desc = input("Nueva descripción (dejar vacío para mantener): ").strip()
            if nueva_desc:
                tarea['descripcion'] = nueva_desc

            # Editar Prioridad
            nueva_prioridad = input("Nueva prioridad (Alta/Media/Baja) o vacío: ").strip().capitalize()
            if nueva_prioridad and validar_prioridad(nueva_prioridad):
                tarea['prioridad'] = nueva_prioridad

            # Editar Fecha Límite
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
    """
    Elimina una tarea del sistema después de confirmación del usuario.
    
    Solicita confirmación antes de eliminar para evitar eliminaciones accidentales.
    Returns:
        None
    """
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
    """
    Busca tareas por palabra clave en título o descripción.

    Realiza una búsqueda insensible a mayúsculas/minúsculas.
    Returns:
        None
    """
    if not tareas:
        print("No hay tareas para buscar.")
        input("Enter...")
        return

    print("\n--- BÚSQUEDA ---")
    palabra_clave = input("Ingresa palabra clave (Título o Descripción): ").lower()
    
    #Búsqueda en título y descripción
    resultados = [t for t in tareas if palabra_clave in t['titulo'].lower() or palabra_clave in t['descripcion'].lower()]
    
    if resultados:
        print(f"\n {len(resultados)} resultado(s) encontrado(s):")
        for tarea in resultados:
            print(f"ID: {tarea['id']} | Título: {tarea['titulo']} | Estado: {tarea['estado']}")
    else:
        print("No se encontraron tareas con esa búsqueda.")
    input("Enter...")

#FUNCIÓN PRINCIPAL

def main():
    """
    Función principal del programa.
    
    Controla el bucle principal del menú y dirige las operaciones
    a las funciones correspondientes según la opción seleccionada.
    Returns:
        None
    """
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