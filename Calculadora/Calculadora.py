def suma_conjuntos(conjuntos):
  """
  Calcula la suma de todos los números en los conjuntos dados.

  Args:
    conjuntos: Una lista de listas de números.

  Returns:
    La suma total de todos los números.
  """
  suma_total = 0
  for conjunto in conjuntos:
    for numero in conjunto:
      suma_total += numero
  return suma_total

def multiplicacion_conjuntos(conjuntos):
  """
  Calcula la multiplicación de todos los números en los conjuntos dados.

  Args:
    conjuntos: Una lista de listas de números.

  Returns:
    El producto total de todos los números.
  """
  producto_total = 1
  for conjunto in conjuntos:
    for numero in conjunto:
      producto_total *= numero
  return producto_total

def division_conjuntos(conjuntos):
  """
  Calcula la división de todos los números en los conjuntos dados, de izquierda a derecha.

  Args:
    conjuntos: Una lista de listas de números.

  Returns:
    El resultado de dividir cada número por el anterior, comenzando por el primer conjunto.
  """
  resultado = conjuntos[0][0]
  for conjunto in conjuntos[1:]:
    for numero in conjunto:
      resultado /= numero
  return resultado

# Solicitar la cantidad de conjuntos de números
cantidad_conjuntos = int(input("¿Cuántos conjuntos de números desea ingresar?: "))

# Ingresar los conjuntos de números
conjuntos = []
for i in range(cantidad_conjuntos):
  conjunto_str = input(f"Ingrese el conjunto {i + 1} (separado por comas): ")
  conjunto = [float(numero) for numero in conjunto_str.split(",")]
  conjuntos.append(conjunto)

# Calcular y mostrar los resultados
suma = suma_conjuntos(conjuntos)
multiplicacion = multiplicacion_conjuntos(conjuntos)
division = division_conjuntos(conjuntos)

print(f"La suma de todos los conjuntos es: {suma}")
print(f"La multiplicación de todos los conjuntos es: {multiplicacion}")
print(f"La división de todos los conjuntos es: {division}")
