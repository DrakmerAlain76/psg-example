# Crea una calculadora por consola que realice las operaciones de suma, resta, multiplicación y división. Las operaciones se ingresan por teclado separadas por comas en el siguiente formato:
# numero1, número2, operación
# ejemplo: 10, 5, +
# verifica si la operación solicitada es válida y muestra el resultado
# Operación: 10, 5, +
# Resultado: 15

entrada = input("Operación: ").strip()

partes = [x.strip() for x in entrada.split(",")]

if len(partes) == 3:
    num1_str, num2_str, operacion = partes

    if num1_str.replace('.', '', 1).isdigit() and num2_str.replace('.', '', 1).isdigit():
        num1 = float(num1_str)
        num2 = float(num2_str)

        if operacion in ['+', '-', '*', '/']:
            if operacion == '+':
                print("Resultado:", num1 + num2)
            elif operacion == '-':
                print("Resultado:", num1 - num2)
            elif operacion == '*':
                print("Resultado:", num1 * num2)
            elif operacion == '/':
                if num2 != 0:
                    print("Resultado:", num1 / num2)
                else:
                    print("Error: División por cero")
        else:
            print("Error: Operación no válida")
    else:
        print("Error: Números no válidos")
else:
    print("Error: Formato incorrecto (usa: número1, número2, operación)")
