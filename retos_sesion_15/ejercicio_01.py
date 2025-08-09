# Crea una calculadora interactiva que solicite dos números 
# por teclado y realice las operaciones 
# de suma, resta, multiplicación y división. El programa debe seguir 
# solicitando dos números hasta que se ingrese "salir". 
# Se debe incluir el manejo de excepciones para evitar errores al ingresar datos no numéricos, 
# al intentar dividir entre cero, o ante cualquier otro error inesperado.

while True:
    try:
        # Solicitar el primer número
        num1 = input("Ingrese el primer número (o 'salir' para terminar): ")
        if num1.lower() == "salir":
            print("Saliendo de la calculadora...")
            break
        num1 = float(num1)

        # Solicitar el segundo número
        num2 = input("Ingrese el segundo número (o 'salir' para terminar): ")
        if num2.lower() == "salir":
            print("Saliendo de la calculadora...")
            break
        num2 = float(num2)

        # Operaciones
        print(f"Suma: {num1} + {num2} = {num1 + num2}")
        print(f"Resta: {num1} - {num2} = {num1 - num2}")
        print(f"Multiplicación: {num1} * {num2} = {num1 * num2}")
        try:
            division = num1 / num2
            print(f"División: {num1} / {num2} = {division}")
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")

    except ValueError:
        print("Error: Ingrese solo números válidos o 'salir'.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
