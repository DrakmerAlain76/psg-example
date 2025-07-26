# Crea un ciclo infinito que reciba un número por teclado y verifique si el número es múltiplo de 7. La ejecución termina si se ingresa el número 0
numero = -1  # Inicializamos con un número distinto de 0

while numero != 0:
    numero = int(input("Ingresa un número (0 para salir): "))

    if numero == 0:
        print("Programa finalizado.")
        break

    if numero % 7 == 0:
        print(f"{numero} es múltiplo de 7.")
    else:
        print(f"{numero} NO es múltiplo de 7.")

