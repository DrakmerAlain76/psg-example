#3 Crear una función recursiva para obtener el N-esimo número de la serie de Lucas

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)
n = 6
print(f"El término {n} de la serie de Lucas es:", lucas(n))
