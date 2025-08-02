#2 Crear una función que reciba dos números y una operación (suma, resta, multiplicación, división) y devuelva el resultado de la operación
# Ejemplo: calcular(10, 5, "+") debe devolver 15

def calcular(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        if num2 == 0:
            return "Error: división entre cero"
        return num1 / num2
    else:
        return "Operación no válida"

resultado = calcular(10, 5, "+")
print("Resultado:", resultado)
