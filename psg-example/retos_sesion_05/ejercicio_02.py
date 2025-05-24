#Escribe un programa en Python que convierta las siguientes temperaturas de grados Fahrenheit a grados Celsius:
#    25 ºF
#    300 ºF
#    76 ºF

# Temperaturas en grados Fahrenheit
f1 = 25
f2 = 300
f3 = 76

# Conversión a grados Celsius usando la fórmula: (F - 32) * 5 / 9
c1 = (f1 - 32) * 5 / 9
c2 = (f2 - 32) * 5 / 9
c3 = (f3 - 32) * 5 / 9

# Mostrar resultados
print(f"{f1} ºF = {c1:.2f} ºC")
print(f"{f2} ºF = {c2:.2f} ºC")
print(f"{f3} ºF = {c3:.2f} ºC")
