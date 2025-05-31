#5 Comparar los números 44 y 98 , 111 y 333 , comprobar si tienen la misma paridad ambos pares o ambos impares

numero1 = 44 % 2 != 0 
numero2 = 98 % 2 != 0
numero3 = 111 % 2 != 0
numero4 = 333 % 2 != 0

print(bool(numero1 and numero2))
print(bool(numero3 and numero4))

