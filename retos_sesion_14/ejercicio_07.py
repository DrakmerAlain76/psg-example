#7 Tres en Raya:
# Crear una función que reciba una jugada en cada ejecución
# Cuando la jugada se completa se debe mostrar el tablero
# El tablero debe ser una lista de listas
# El juego termina cuando un jugador gana o hay un empate
# Si una casilla ya está ocupada, se debe pedir una nueva jugada
# Se debe mostrar a quién le toca jugar, si a "X" o "O"
# tres_en_raya("X", 0, 0)

# [['X', ' ', ' '],
#  [' ', ' ', ' '],
#  [' ', ' ', ' ']]


def mostrar_tablero(tablero):
    for fila in tablero:
        print(fila)

def hay_ganador(tablero, jugador):
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)) or \
           all(tablero[j][i] == jugador for j in range(3)):
            return True
    if all(tablero[i][i] == jugador for i in range(3)) or \
       all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    return False

def hay_empate(tablero):
    return all(casilla != " " for fila in tablero for casilla in fila)

def jugar():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    turno_actual = "X"
    juego_terminado = False

    while not juego_terminado:
        mostrar_tablero(tablero)
        print(f"Turno de '{turno_actual}'")
        
        try:
            fila = int(input("Ingresa la fila (0-2): "))
            columna = int(input("Ingresa la columna (0-2): "))
        except ValueError:
            print("❌ Entrada inválida. Ingresa números.")
            continue

        if not (0 <= fila < 3 and 0 <= columna < 3):
            print("❌ Posición fuera del tablero. Intenta de nuevo.")
            continue

        if tablero[fila][columna] != " ":
            print("❌ Casilla ocupada. Intenta otra.")
            continue

        tablero[fila][columna] = turno_actual

        if hay_ganador(tablero, turno_actual):
            mostrar_tablero(tablero)
            print(f"🎉 ¡Jugador '{turno_actual}' gana!")
            juego_terminado = True
        elif hay_empate(tablero):
            mostrar_tablero(tablero)
            print("🤝 ¡Empate!")
            juego_terminado = True
        else:
            turno_actual = "O" if turno_actual == "X" else "X"

jugar()
