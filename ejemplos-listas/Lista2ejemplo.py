# listas/ejemplo2.py

# Crear una lista de números
numeros = [5, 3, 9, 1, 4]

# Eliminar el último elemento
numeros.pop()

# Invertir el orden de la lista
numeros.reverse()

# Filtrar elementos mayores que 4
numeros_filtrados = [num for num in numeros if num > 4]

# Imprimir la lista filtrada
print(numeros_filtrados)
