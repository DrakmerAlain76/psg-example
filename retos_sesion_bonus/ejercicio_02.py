#2 Tienes un juego de adivinanzas en el que el jugador tiene que adivinar un número entre 1 y 100. 
# El juego tiene bugs, arréglalos!

import random
def obtener_aleatorio():
    # se corrige el rango del número aleatorio
    return random.randint(1, 100)

def adivina(secreto):
    intentos = 0
    print("¿Qué número estoy pensando? (1-100)")
    while True:
        try:            
            intento = int(input(f"Intento N° {intentos + 1}: "))
            intentos += 1

            if intento == secreto:
                print("¡Felicidades! ¡Has adivinado el número!")
                break
            elif intento < secreto:
                print("El número es mayor.")
            else:
                print("El número es menor.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    #se corrige la los intentos (se multiplicaba por 10) y opcion si es a la primera
    print(f"Has adivinado el número en {intentos} intento{'s' if intentos != 1 else ''}.\n")

def jugar():
    print("¡Bienvenido al juego de adivinanzas del Python Study Group 2025!")
    print("="*63)
    nombre_jugador = input("¿Cuál es tu nombre?: ").strip() or "Guest"
    print(f"¡Bienvenido, {nombre_jugador}!")
    print("="*63)
    print()

    while True:
        opcion = input("¿Quieres jugar? (s/n): ").strip().lower()
        # entre a jugar, antes no se podia solo con mayusculas
        if opcion != "s":
            break
        secreto = obtener_aleatorio()
        adivina(secreto)

    print("¡Gracias por participar!")
    print(f"🐍 ¡Gracias {nombre_jugador.upper()} por ser parte del Python Study Group 2025! 🐍")

jugar()