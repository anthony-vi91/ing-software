# gestor_sencillo.py
import os
from datetime import datetime

tareas = []
id_counter = 1

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ahora():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def validar_prioridad(p):
    return p in ('Alta', 'Media', 'Baja')

def input_prioridad(prompt="Prioridad (Alta/Media/Baja): "):
    p = input(prompt).strip().capitalize()
    return p if validar_prioridad(p) else None

def mostrar_menu():
    clear()
    print("=== GESTOR SENCILLO DE TAREAS ===")
    print("1 Agregar  2 Ver todas  3 Pendientes  4 Completadas")
    print("5 Marcar completada  6 Editar  7 Eliminar  8 Buscar  9 Salir")

def agregar_tarea():
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
    tarea = {
        'id': id_counter, 'titulo': titulo, 'descripcion': descripcion,
        'prioridad': prioridad, 'estado': 'Pendiente',
        'fecha_creacion': ahora(), 'fecha_limite': fecha_limite
    }
    tareas.append(tarea)
    id_counter += 1
    print(f"Tarea #{tarea['id']} creada.")
    input("Enter...")

def listar(lista, encabezado):
    clear()
    print(encabezado)
    if not lista:
        print("No hay tareas.")
    else:
        print(f"{'ID':<4}{'TÍTULO':<25}{'PRIO':<7}{'EST':<10}{'LÍMITE'}")
        for t in lista:
            print(f"{t['id']:<4}{t['titulo'][:24]:<25}{t['prioridad']:<7}{t['estado']:<10}{t['fecha_limite']}")
    input("Enter...")

def ver_todas():
    listar(tareas, "Todas las tareas")

def ver_pendientes():
    listar([t for t in tareas if t['estado']=='Pendiente'], "Tareas pendientes")

def ver_completadas():
    listar([t for t in tareas if t['estado']=='Completada'], "Tareas completadas")

def buscar_por_id(id_):
    return next((t for t in tareas if t['id']==id_), None)

def marcar_completada():
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

def main():
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
