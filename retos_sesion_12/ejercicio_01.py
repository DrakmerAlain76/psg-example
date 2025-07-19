# 1 Crear un script que pida un número entero y verifique si es múltiplo de 5 usando operador ternario.


numero = int(input("Ingresa un número entero: "))


resultado = "Es múltiplo de 5" if numero % 5 == 0 else "No es múltiplo de 5"

# Mostrar resultado
print(resultado)
