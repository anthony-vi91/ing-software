"""
Sistema de Análisis de Números Aleatorios 
Programa educativo para practicar documentación con docstrings. 
Autor: Anthony Alexander Vite Amon
Fecha: 19/03/2026
""" 
import random

def generar_numero_aleatorio(inicio, fin): 
    """
    Genera un número aleatorio dentro del rango especificado.
    
    Args:
        inicio (int): Límite inferior del rango (incluido).
        fin (int): Límite superior del rango (incluido).
    
    Returns:
        int: Número aleatorio en el rango [inicio, fin].
    """
    return random.randint(inicio, fin) 

def es_par(numero): 
    """
    Determina si un número es par.
    
    Args:
        numero (int): Número a evaluar.
    
    Returns:
        bool: True si es par, False si es impar.
    """
    return numero % 2 == 0 

def calcular_estadisticas(lista_numeros): 
    """
    Calcula estadísticas de una lista de números.
    
    Args:
        lista_numeros (list): Lista de números enteros.
    
    Returns:
        tuple: (promedio, máximo, cantidad_pares)
    """
    if not lista_numeros: 
        return (0.0, None, 0) 
    promedio = sum(lista_numeros) / len(lista_numeros) 
    maximo = max(lista_numeros) 
    cantidad_pares = sum(1 for num in lista_numeros if es_par(num)) 
    return promedio, maximo, cantidad_pares 

def generar_reporte(cantidad=10, rango_inicio=1, rango_fin=100): 
    """
    Genera y muestra un reporte completo de números aleatorios.
    
    Args:
        cantidad (int): Cantidad de números a generar (default: 10).
        rango_inicio (int): Límite inferior (default: 1).
        rango_fin (int): Límite superior (default: 100).
    
    Returns:
        tuple: (lista_numeros, promedio, maximo, pares)
    """
    numeros = [generar_numero_aleatorio(rango_inicio, rango_fin)
               for _ in range(cantidad)] 
    promedio, maximo, pares = calcular_estadisticas(numeros) 
    print(f"REPORTE DE ANÁLISIS")
    print(f"{'='*40}")
    print(f"Números generados: {numeros}")
    print(f"Cantidad total: {len(numeros)}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Valor máximo: {maximo}")
    print(f"Números pares: {pares}")
    print(f"Números impares: {len(numeros) - pares}")
    return numeros, promedio, maximo, pares 

def main(): 
    """
    Función principal que ejecuta el programa completo.
    """
    print("Sistema de Análisis de Números Aleatorios")
    print("=" * 50)
    
    # ✅ EJECUTAR AQUÍ LAS FUNCIONES
    print("\n--- REPORTE POR DEFECTO ---")
    generar_reporte()
    
    print("\n" + "=" * 50)
    print("\n--- REPORTE PERSONALIZADO ---")
    generar_reporte(cantidad=5, rango_inicio=10, rango_fin=50)

if __name__ == "__main__":
    main() 