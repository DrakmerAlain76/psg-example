# Imprimir un tablero de ajedrez de 8x8 con los caracteres # y *
for fila in range(8):
    linea = ""
    for columna in range(8):
        if (fila + columna) % 2 == 0:
            linea += "#"
        else:
            linea += "*"
    print(linea)
