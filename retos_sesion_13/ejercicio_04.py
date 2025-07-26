# Crea un ciclo infinito que reciba una frase por teclado y verifique si la frase es palíndromo. La ejecución termina si la frase ingresada contiene la palabra salir
frase = ""

while "salir" not in frase.lower():
    frase = input("Ingresa una frase (o escribe 'salir' para terminar): ").lower()

    if "salir" in frase:
        print("Programa finalizado.")
        break

    # Eliminar espacios y caracteres no alfanuméricos
    frase_limpia = ''.join(c for c in frase if c.isalnum())

    if frase_limpia == frase_limpia[::-1]:
        print("✅ La frase es un palíndromo.")
    else:
        print("❌ La frase NO es un palíndromo.")
