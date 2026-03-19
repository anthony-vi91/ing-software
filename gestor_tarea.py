import os
from datetime import datetime

# ==============================
# GESTOR DE TAREAS PERSONALES
# ==============================

#Autores: Anthony Vite - Emily Alvarez

tareas = []       # Lista global donde se almacenan las tareas
id_counter = 1    # Contador para asignar IDs únicos a cada tarea

# Funciones Adicionales
def clear():
    """
    Limpia la pantalla según el sistema operativo.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def ahora():
    """
    Devuelve la fecha y hora actual en formato YYYY-MM-DD HH:MM.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def validar_prioridad(p):
    """
    Valida que la prioridad ingresada sea Alta, Media o Baja.
    """
    return p in ('Alta', 'Media', 'Baja')

def input_prioridad(prompt="Prioridad (Alta/Media/Baja): "):
    """
    Solicita al usuario una prioridad válida.
    """
    p = input(prompt).strip().capitalize()
    return p if validar_prioridad(p) else None

# Menú principal
def mostrar_menu():
    """Muestra el menú principal."""
    clear()
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

# CRUD de tareas
def agregar_tarea():
    """
    Agrega una nueva tarea a la lista.
    """
    global id_counter
    print("\nAgregar tarea")
    titulo = input("Título: ").strip()
    if not titulo:
        print("Título vacío. Cancelado.")
        input("Enter...")
        return
    descripcion = input("Descripción (opcional): ").strip()
    prioridad = None
    while prioridad is None:
        prioridad = input_prioridad()
        if prioridad is None:
            print("Prioridad inválida.")
    fecha_limite = input("Fecha límite (YYYY-MM-DD) o vacío: ").strip() or "Sin límite"
    
    # Crear diccionario con los datos de la tarea
    tarea = {
        'id': id_counter, 'titulo': titulo, 'descripcion': descripcion,
        'prioridad': prioridad, 'estado': 'Pendiente',
        'fecha_creacion': ahora(), 'fecha_limite': fecha_limite
    }
    tareas.append(tarea)   # Agregar tarea a la lista
    id_counter += 1        # Incrementar contador de IDs
    print(f"Tarea #{tarea['id']} creada.")
    input("Enter...")

def listar(lista, encabezado):
    """
    Muestra una lista de tareas con formato tabular.
    """
    clear()
    print(encabezado)
    if not lista:
        print("No hay tareas.")
    else:
        print(f"{'ID':<5}{'TÍTULO':<25}{'PRIORIDAD':<10}{'ESTADO':<12}")
        for t in lista:
            #Mostrar de forma ordenada los datos de id-titulo-prioridad-estado.
            print(f"{t['id']:<5}{t['titulo'][:24]:<25}{t['prioridad']:<10}{t['estado']:<12}")
    input("Enter...")

def ver_todas():
    """
    Muestra todas las tareas registradas.
    """
    listar(tareas, "Todas las tareas")

def ver_pendientes():
    """
    Muestra solo las tareas pendientes.
    """
    listar([t for t in tareas if t['estado']=='Pendiente'], "Tareas pendientes")

def ver_completadas():
    """
    Muestra solo las tareas completadas.
    """
    listar([t for t in tareas if t['estado']=='Completada'], "Tareas completadas")

def buscar_por_id(id_):
    """
    Busca una tarea por su ID y la devuelve si existe.
    """
    return next((t for t in tareas if t['id']==id_), None)

def marcar_completada():
    """
    Permite marcar una tarea como completada.
    """
    if not tareas:
        print("No hay tareas.")
        input("Enter..."); return
    ver_todas()
    try:
        i = int(input("ID a marcar: "))
        t = buscar_por_id(i)
        if t:
            t['estado'] = 'Completada'
            print("Marcada como completada.")
        else:
            print("ID no encontrado.")
    except ValueError:
        print("Entrada inválida.")
    input("Enter...")

def editar_tarea():
    """
    Permite editar los datos de una tarea existente.
    """
    if not tareas:
        print("No hay tareas.")
        input("Enter..."); return
    ver_todas()
    try:
        i = int(input("ID a editar: "))
        t = buscar_por_id(i)
        if not t:
            print("ID no encontrado.")
            input("Enter..."); return
        
        #Actualizar campos si el usuario ingresa nuevos valores
        nt = input("Nuevo título (vacío para mantener): ").strip()
        if nt: t['titulo'] = nt
        nd = input("Nueva descripción (vacío para mantener): ").strip()
        if nd: t['descripcion'] = nd
        np = input("Nueva prioridad (Alta/Media/Baja) o vacío: ").strip().capitalize()
        if np and validar_prioridad(np): t['prioridad'] = np
        nl = input("Nueva fecha límite o vacío: ").strip()
        if nl: t['fecha_limite'] = nl
        print("Tarea actualizada.")
    except ValueError:
        print("Entrada inválida.")
    input("Enter...")

def eliminar_tarea():
    """
    Elimina una tarea seleccionada por ID.
    """
    if not tareas:
        print("No hay tareas.")
        input("Enter..."); return
    ver_todas()
    try:
        i = int(input("ID a eliminar: "))
        t = buscar_por_id(i)
        if t:
            if input(f"Eliminar '{t['titulo']}'? (s/n): ").lower() == 's':
                tareas.remove(t)
                print("Eliminada.")
            else:
                print("Cancelado.")
        else:
            print("ID no encontrado.")
    except ValueError:
        print("Entrada inválida.")
    input("Enter...")

def buscar_tareas():
    """
    Busca tareas por palabra clave en título o descripción.
    """
    if not tareas:
        print("No hay tareas.")
        input("Enter..."); return
    k = input("Palabra clave: ").lower().strip()
    res = [t for t in tareas if k in t['titulo'].lower() or k in t['descripcion'].lower()]
    if res:
        for t in res:
            print(f"ID:{t['id']} Título:{t['titulo']} Estado:{t['estado']}")
    else:
        print("No se encontraron coincidencias.")
    input("Enter...")

#Función principal
def main():
    """
    Bucle del programa que gestiona el menú y las opciones.
    """
    while True:
        mostrar_menu()
        opt = input("Opción: ").strip()
        if opt == '1': agregar_tarea()
        elif opt == '2': ver_todas()
        elif opt == '3': ver_pendientes()
        elif opt == '4': ver_completadas()
        elif opt == '5': marcar_completada()
        elif opt == '6': editar_tarea()
        elif opt == '7': eliminar_tarea()
        elif opt == '8': buscar_tareas()
        elif opt == '9':
            print("Adiós")
            break
        else:
            print("Opción inválida.")
            input("Enter...")

if __name__ == "__main__":
    main()