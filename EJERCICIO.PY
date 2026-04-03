"""
Programa para calcular el salario de un profesor
con incremento anual del 10% durante 6 años.
Cumple PEP8 y usa docstrings para documentación.
"""

def calcular_salario(inicial: float, incremento: float, años: int) -> list:
    """
    Calcula el salario año por año.

    Args:
        inicial (float): Salario inicial.
        incremento (float): Porcentaje de incremento anual.
        años (int): Número de años.

    Returns:
        list: Lista con los salarios de cada año.
    """
    salarios = []
    salario = inicial
    for _ in range(años):
        salarios.append(round(salario, 2))
        salario *= (1 + incremento)
    return salarios


def mostrar_salarios(salarios: list) -> None:
    """
    Muestra los salarios año por año y el final.

    Args:
        salarios (list): Lista de salarios calculados.
    """
    for i, s in enumerate(salarios, start=1):
        print(f"Año {i}: ${s:.2f}")
    print(f"Salario final después de {len(salarios)} años: ${salarios[-1]:.2f}")


# Ejecución del programa
if __name__ == "__main__":
    resultado = calcular_salario(1500, 0.10, 6)
    mostrar_salarios(resultado)
