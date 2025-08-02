#5 Crear una función que reciba una cadena y devuelva la cantidad de vocales que tiene.

def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador

texto = "Hola mundo desde Python"
print("Cantidad de vocales:", contar_vocales(texto))  # Resultado: 4
