import os
from datetime import datetime

# Variables globales documentadas
#: Lista global que almacena todas las tareas como diccionarios
tareas = []
#: Contador global para generar IDs únicos incrementales
id_counter = 1


def clear() -> None:
    """
    Limpia la pantalla de la terminal de forma multiplataforma.

    Detecta el sistema operativo y ejecuta el comando apropiado:
    - Windows (nt): 'cls'
    - Unix/Linux/Mac: 'clear'
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def ahora() -> str:
    """
    Obtiene la fecha y hora actual en formato estandarizado.

    Returns:
        str: Fecha y hora en formato 'YYYY-MM-DD HH:MM'
             Ejemplo: '2024-01-15 14:30'
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def validar_prioridad(p: str) -> bool:
    """
    Valida que la prioridad ingresada sea una de las opciones permitidas.

    Args:
        p (str): Prioridad a validar (debe coincidir exactamente)

    Returns:
        bool: True si p es 'Alta', 'Media' o 'Baja', False en otro caso
    """
    return p in ('Alta', 'Media', 'Baja')


def input_prioridad(prompt: str = "Prioridad (Alta/Media/Baja): ") -> str | None:
    """
    Solicita al usuario una prioridad válida con validación automática.

    Args:
        prompt (str, optional): Mensaje personalizado para el input.
                               Defaults to "Prioridad (Alta/Media/Baja): ".
    """
    p = input(prompt).strip().capitalize()
    return p if validar_prioridad(p) else None


def mostrar_menu() -> None:
    """
    Muestra el menú principal con todas las opciones disponibles.

    Limpia la pantalla primero y muestra un menú numerado del 1 al 9 con:
    1. Agregar nueva tarea
    2. Ver todas las tareas
    3. Ver solo tareas pendientes
    4. Ver solo tareas completadas
    5. Marcar tarea como completada
    6. Editar tarea
    7. Eliminar tarea
    8. Buscar tareas
    9. Salir del programa
    """
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


def agregar_tarea() -> None:
    """
    Crea una nueva tarea interactivamente y la agrega a la lista global.

    Solicita:
    - Título (obligatorio)
    - Descripción (opcional)
    - Prioridad (Alta/Media/Baja con validación)
    - Fecha límite (opcional, formato YYYY-MM-DD)

    La tarea se guarda como diccionario con:
    - id: ID único autoincremental
    - titulo: str
    - descripcion: str
    - prioridad: str ('Alta', 'Media', 'Baja')
    - estado: str ('Pendiente' por defecto)
    - fecha_creacion: str (timestamp automático)
    - fecha_limite: str
    """
    global id_counter
    print("\nAgregar tarea")
    titulo = input("Título: ").strip()
    if not titulo:
        print("Título vacío. Cancelado.")
        input("Enter...")
        return

    descripcion = input("Descripción (opcional): ").strip()

    # Validación de prioridad con reintento automático
    prioridad = None
    while prioridad is None:
        prioridad = input_prioridad()
        if prioridad is None:
            print("Prioridad inválida.")

    fecha_limite = input("Fecha límite (YYYY-MM-DD) o vacío: ").strip() or "Sin límite"

    # Crear estructura de tarea completa
    tarea = {
        'id': id_counter,
        'titulo': titulo,
        'descripcion': descripcion,
        'prioridad': prioridad,
        'estado': 'Pendiente',
        'fecha_creacion': ahora(),
        'fecha_limite': fecha_limite
    }

    tareas.append(tarea)
    id_counter += 1
    print(f"Tarea #{tarea['id']} creada.")
    input("Enter...")


def listar(lista: list, encabezado: str) -> None:
    """
    Muestra una tabla formateada de tareas con columnas alineadas.

    Args:
        lista (list): Lista de diccionarios de tareas a mostrar
        encabezado (str): Título descriptivo de la vista

    Formato de tabla:
    ID    TÍTULO                 PRIORIDAD  ESTADO
    1     Comprar leche          Alta       Pendiente
    """
    clear()
    print(encabezado)
    if not lista:
        print("No hay tareas.")
    else:
        print(f"{'ID':<5}{'TÍTULO':<25}{'PRIORIDAD':<10}{'ESTADO':<12}")
        print("-" * 52)
        for t in lista:
            print(f"{t['id']:<5}{t['titulo'][:24]:<25}{t['prioridad']:<10}{t['estado']:<12}")
    input("Enter...")


def ver_todas() -> None:
    """Visualiza todas las tareas registradas en formato de tabla."""
    listar(tareas, "=== TODAS LAS TAREAS ===")


def ver_pendientes() -> None:
    """Visualiza únicamente las tareas con estado 'Pendiente'."""
    pendientes = [t for t in tareas if t['estado'] == 'Pendiente']
    listar(pendientes, "=== TAREAS PENDIENTES ===")


def ver_completadas() -> None:
    """Visualiza únicamente las tareas con estado 'Completada'."""
    completadas = [t for t in tareas if t['estado'] == 'Completada']
    listar(completadas, "=== TAREAS COMPLETADAS ===")


def buscar_por_id(id_: int) -> dict | None:
    """
    Busca una tarea específica por su ID único.

    Args:
        id_ (int): Identificador numérico único de la tarea
    """
    return next((t for t in tareas if t['id'] == id_), None)


def marcar_completada() -> None:
    """
    Cambia el estado de una tarea de 'Pendiente' a 'Completada'.

    Muestra todas las tareas primero, solicita ID y valida existencia.
    """
    if not tareas:
        print("No hay tareas.")
        input("Enter...")
        return

    ver_todas()
    try:
        i = int(input("ID a marcar como completada: "))
        t = buscar_por_id(i)
        if t:
            t['estado'] = 'Completada'
            print(f"Tarea '{t['titulo']}' marcada como completada.")
        else:
            print("ID no encontrado.")
    except ValueError:
        print("Entrada inválida (debe ser un número).")
    input("Enter...")


def editar_tarea() -> None:
    """
    Edita los campos de una tarea existente por ID.

    Permite modificar:
    - Título (vacío = sin cambio)
    - Descripción (vacío = sin cambio)
    - Prioridad (vacío = sin cambio, validación incluida)
    - Fecha límite (vacío = sin cambio)
    """
    if not tareas:
        print("No hay tareas.")
        input("Enter...")
        return

    ver_todas()
    try:
        i = int(input("ID a editar: "))
        t = buscar_por_id(i)
        if not t:
            print("ID no encontrado.")
            input("Enter...")
            return

        # Edición campo por campo (campo vacío preserva valor actual)
        nt = input("Nuevo título (vacío=sin cambio): ").strip()
        if nt:
            t['titulo'] = nt

        nd = input("Nueva descripción (vacío=sin cambio): ").strip()
        if nd:
            t['descripcion'] = nd

        np = input("Nueva prioridad (Alta/Media/Baja) o vacío: ").strip().capitalize()
        if np and validar_prioridad(np):
            t['prioridad'] = np
        elif np:
            print("Prioridad inválida, sin cambios.")

        nl = input("Nueva fecha límite (YYYY-MM-DD) o vacío: ").strip()
        if nl:
            t['fecha_limite'] = nl

        print("Tarea actualizada correctamente.")
    except ValueError:
        print("Entrada inválida.")
    input("Enter...")


def eliminar_tarea() -> None:
    """
    Elimina una tarea específica con confirmación del usuario.

    Requiere confirmación explícita ('s') antes de eliminar permanentemente.
    """
    if not tareas:
        print("No hay tareas.")
        input("Enter...")
        return

    ver_todas()
    try:
        i = int(input("ID a eliminar: "))
        t = buscar_por_id(i)
        if t:
            confirm = input(f"¿Eliminar '{t['titulo']}' permanentemente? (s/n): ").lower()
            if confirm == 's':
                tareas.remove(t)
                print("🗑️ Tarea eliminada permanentemente.")
            else:
                print("Eliminación cancelada.")
        else:
            print("ID no encontrado.")
    except ValueError:
        print("Entrada inválida.")
    input("Enter...")


def buscar_tareas() -> None:
    """
    Busca tareas por palabra clave en título o descripción.

    Búsqueda case-insensitive que muestra resultados con ID, título y estado.
    """
    if not tareas:
        print("No hay tareas.")
        input("Enter...")
        return

    k = input("Palabra clave para buscar: ").lower().strip()
    if not k:
        print("Palabra clave vacía.")
        input("Enter...")
        return

    res = [
        t for t in tareas 
        if k in t['titulo'].lower() or k in t['descripcion'].lower()
    ]

    clear()
    print(f"=== RESULTADOS DE BÚSQUEDA: '{k}' ===")
    if res:
        print(f"{'ID':<4} {'TÍTULO':<30} {'ESTADO'}")
        print("-" * 40)
        for t in res:
            print(f"{t['id']:<4} {t['titulo'][:29]:<30} {t['estado']}")
    else:
        print("No se encontraron coincidencias.")
    input("Enter...")


def main() -> None:
    """
    Bucle principal del programa - Menú interactivo infinito.

    Ejecuta el menú en bucle hasta que el usuario seleccione opción 9 (Salir).
    Maneja todas las opciones del 1 al 9 con validación de entrada.
    """
    print("GESTOR DE TAREAS PERSONALES iniciado correctamente.")
    try:
        while True:
            mostrar_menu()
            opt = input("Selecciona una opción (1-9): ").strip()
            
            if opt == '1':
                agregar_tarea()
            elif opt == '2':
                ver_todas()
            elif opt == '3':
                ver_pendientes()
            elif opt == '4':
                ver_completadas()
            elif opt == '5':
                marcar_completada()
            elif opt == '6':
                editar_tarea()
            elif opt == '7':
                eliminar_tarea()
            elif opt == '8':
                buscar_tareas()
            elif opt == '9':
                clear()
                print("Adiós.")
                break
            else:
                print(" Opción inválida. Selecciona del 1 al 9.")
                input("Presiona Enter para continuar...")
    except KeyboardInterrupt:
        print("\n\n Programa interrumpido por el usuario. Adiós.")
    except Exception as e:
        print(f"\n Error inesperado: {e}")


if __name__ == "__main__":
    main()
