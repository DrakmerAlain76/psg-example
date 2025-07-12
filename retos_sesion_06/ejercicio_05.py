#5 Comparar los números 44 y 98 , 111 y 333 , comprobar si tienen la misma paridad ambos pares o ambos impares

# Comparar paridad entre 44 y 98
mismo_paridad_1 = (44 % 2) == (98 % 2)

# Comparar paridad entre 111 y 333
mismo_paridad_2 = (111 % 2) == (333 % 2)

print("¿44 y 98 tienen la misma paridad?", mismo_paridad_1)
print("¿111 y 333 tienen la misma paridad?", mismo_paridad_2)
