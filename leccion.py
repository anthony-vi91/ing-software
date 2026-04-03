def clasificar_ventas(ventas):
    """
    Clasifica las ventas en tres categorías y calcula los montos.

    Parámetros
    ventas : list of float
        Lista con los valores de cada venta realizada.
    """
    resultado = {
        "mayores_1000": {"cantidad": 0, "monto": 0.0},
        "entre_501_1000": {"cantidad": 0, "monto": 0.0},
        "menores_500": {"cantidad": 0, "monto": 0.0},
        "total_global": 0.0
    }

    for venta in ventas:
        if venta > 1000:
            resultado["mayores_1000"]["cantidad"] += 1
            resultado["mayores_1000"]["monto"] += venta
        elif venta > 500:
            resultado["entre_501_1000"]["cantidad"] += 1
            resultado["entre_501_1000"]["monto"] += venta
        else:
            resultado["menores_500"]["cantidad"] += 1
            resultado["menores_500"]["monto"] += venta

        resultado["total_global"] += venta

    return resultado


def mostrar_resultados(resultado):
    """
    Muestra en pantalla los resultados de la clasificación de ventas.
    """
    print("---- Resultados de las Ventas ----")
    print(f"Ventas mayores a $1000: {resultado['mayores_1000']['cantidad']} "
          f"(Monto: ${resultado['mayores_1000']['monto']:.2f})")
    print(f"Ventas entre $501 y $1000: {resultado['entre_501_1000']['cantidad']} "
          f"(Monto: ${resultado['entre_501_1000']['monto']:.2f})")
    print(f"Ventas menores o iguales a $500: {resultado['menores_500']['cantidad']} "
          f"(Monto: ${resultado['menores_500']['monto']:.2f})")
    print(f"Monto total global: ${resultado['total_global']:.2f}")


def main():
    """
    Función principal del programa.

    Permite ingresar N ventas por teclado y muestra los resultados
    de la clasificación.
    """
    try:
        n = int(input("Ingrese el número de ventas realizadas: "))
        ventas = []

        for i in range(n):
            monto = float(input(f"Ingrese el monto de la venta {i+1}: "))
            if monto < 0:
                print("Error: el monto no puede ser negativo.")
                return
            ventas.append(monto)

        resultado = clasificar_ventas(ventas)
        mostrar_resultados(resultado)

    except ValueError:
        print("Error: debe ingresar valores numéricos válidos.")


if __name__ == "__main__":
    main()
