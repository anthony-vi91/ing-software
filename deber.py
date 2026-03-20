"""
Sistema de Análisis de Números Aleatorios 
Programa educativo para practicar documentación con docstrings. 
Autor: Anthony Alexander Vite Amon
Fecha: 19/03/2026
""" 
import random #Importa una funcion que genera numeros aleatorios 
def generar_numero_aleatorio (inicio, fin): 
    """
    Esta funcion genera un numero aleatorio dentro del rango que se designe de inicio a fin
    
    Agr: Ingresa un numero aleatorio en el rango de inicio hasta fin 
         Random.randit se encarga de que los numeros ingresados sean aleatorios.
    Returns: None

    """
    return random.randint(inicio, fin) 
def es_par(numero): 
    """
    Esta funcion se encarga de determinar si el numero ingresado es par o no.
    
    Agr: Ingresa el numero aleatorio en la funciones de inicio a fin.
    Returns: None.

    """
    return numero % 2 == 0 
def calcular_estadisticas (lista_numeros): 
    """
    La funcion calcular_estadistica se encarga de calcular el promedio para definir si es par o impar
    
    Agr:Ingresa de los numeros aleatorio para calcular el promedio y la cantidad de numeros en el rango para asi sacar y definir si los numeros en ese rango son pares o impares.
    Returns: None.

    """
    if not lista_numeros: 
        return (0.0, None, 0) 
    promedio = sum(lista_numeros) / len(lista_numeros) 
    maximo = max(lista_numeros) 
    cantidad_pares = sum (1 for num in lista_numeros if es_par (num)) 
    return promedio, maximo, cantidad_pares 

def generar_reporte(cantidad=10, rango_inicio=1, rango_fin=100): 
    """
    Funcion que permite generar la vizualizacion de los numeros generados, cantidad, promedio, maximo y pares.
    Con ella llama a todas las funciones creadas para poder presentarlas junto con el texto correspondiente.
    
    Agr:Promedio, Numeros Pares, Cantidad Maxima y el total de numeros generados de forma aleatoria.
    Llama a los numeros para poder calcular en el rango de los numeros inicio y fin
    evalua el promedio de los numeros de inicio y fin
    da como resultado el valor maximo y el numero de pares.
    y presenta todo junto con el texto correspondiente.

    Returns: None.
    """
    numeros = [generar_numero_aleatorio(rango_inicio, rango_fin)
    for _ in range(cantidad)] 
    promedio, maximo, pares = calcular_estadisticas (numeros) 
    print (f"REPORTE DE ANÁLISIS") 
    print (f"{'='*40}") 
    print (f"Números generados: {numeros}") 
    print (f"Cantidad total: {len (numeros)}") 
    print (f"Promedio: {promedio:.2f}") 
    print (f"Valor máximo: {maximo}") 
    print (f"Números pares: {pares}") 
    print (f"Números impares: {len (numeros) - pares}") 
    return numeros, promedio, maximo, pares 
def main(): 
    """
    El main se encarga de llevar todo los calculos de generacion de reporte y presentacion de los mismos.
    Todo esto es par ala vizualizacion del programa
    Tambien con ella se guardan los numeros ingresados del 1 al 100 de forma aleatoria.
    Agr: Generar reporte de numeros aleatorios.
    
    Returns: None.
    """
    print("Sistema de Análisis de Números Aleatorios") 
    print("=" * 50) 
# Generar reporte con valores por defecto 
generar_reporte() 
print("\n" + "=" * 50) 
# Generar reporte personalizado 
generar_reporte (cantidad=5, rango_inicio=10, rango_fin=50) 
if __name == "__main__": 
    main() 
