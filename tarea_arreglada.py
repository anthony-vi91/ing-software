def calcular_salarios():
  """
  Funcion que calcula los salarios de un profesor con incremento anual.

  Parametros:
  - salario_inicial = 1500
  - incremento = 10% anual
  - duracion = 6 años
  """
  salario_inicial = 1500    # Salario base inicial
  incremento = 0.10         # Porcentaje de incremento anual
  salarios = []             # Lista para almacenar salarios año por año
  
  salario_actual = salario_inicial
  for año in range(1, 7):  # Itera desde año 1 hasta año 6
    salarios.append(salario_actual)  # Guarda el salario del año actual
    salario_actual *= (1 + incremento)  # Aplica incremento para el siguiente año
    
    # El salario final es el ultimo de la lista
    salario_final = salarios[-1]
    return salarios, salario_final

def mostrar_resultados(salarios, salario_final):
  """
  Funcion que muestra los resultados en pantalla.

  Parametros:
  - salarios: listas con los salarios de cada año.
  - salario_final: salario al cabo de 6 años.

  """
  print("-----SALARIOS DEL PROFESOR-----")
  print("Año/Salario")
  print("-" * 30)
  for i, salario in enumerate(salarios , 1):
    # Muestra cada año con formato monetario
    print(f"Año {i}\t${salario:,.2f}")

  print("-" * 30)
  print(f"SALARIO FINAL (6 años): ${salario_final:,.2f}")

def main():
  """
  Funcion principal del programa.
  Llama a las funciones de calculo y muestra resultados.
  """
  print("Programa: Calculo de salario con 10% incremento anual")
  print("=" * 50)

  salarios, salario_final = calcular_salarios()
  mostrar_resultados(salarios, salario_final)

if __name__=="__main__":
  main()