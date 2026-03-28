def calcular_salarios():
  salario_inicial = 1500
  incremento = 0.10
  salarios = [] 
  
  salario_actual = salario_inicial
  for año in range(1, 7):
    salarios.append(salario_actual)
    salario_actual *= (1 + incremento)

    salario_final = salarios[-1]
    return salarios, salario_final

def mostrar_resultados(salarios, salario_final):
  print("-----SALARIOS DEL PROFESOR-----")
  print("Año/Salario")
  print("-" * 30)
  for i, salario in enumerate(salarios , 1):
    print(f"Año {i}\t${salario:,.2f}")

  print("-" * 30)
  print(f"SALARIO FINAL (6 años): ${salario_final:,.2f}")

def main():
  print("Programa: Calculo de salario con 10% incremento anual")
  print("=" * 50)

  salarios, salario_final = calcular_salarios()
  mostrar_resultados(salarios, salario_final)

if __name__=="__main__":
  main()