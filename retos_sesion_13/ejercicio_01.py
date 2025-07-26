# Imprimir los 20 primeros números de la sucesión de Lucas.

lucas = [2, 1]  # Los dos primeros términos

# Generar los siguientes 18 términos
for i in range(2, 20):
    siguiente = lucas[i - 1] + lucas[i - 2]
    lucas.append(siguiente)

# Imprimir el resultado
print("Los 20 primeros números de la sucesión de Lucas son:")
print(lucas)
