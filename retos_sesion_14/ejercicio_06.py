#6 Crear una función que reciba una lista de números y devuelva una lista
# con los números pares y otra lista con los números impares

def separar_pares_impares(numeros):
    pares = []
    impares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = separar_pares_impares(lista)

print("Números pares:", pares)
print("Números impares:", impares)
