# 2 Crea una tupla con los siguientes elementos:
# 'a','b','c','d','e','f','g','h','i','j'

#     Imprime el primer elemento
#     Imprime el último elemento
#     Imprime un slice del índice 3 al 5
#     Imprime un slice del 5 al 9 con pasos de 3
#     Imprime un slice del 9 al 0 con pasos de -2

tupla = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print("Primer elemento:", tupla[0])
print("Último elemento:", tupla[-1])
print("Slice del índice 3 al 5:", tupla[3:6])
print("Slice del 5 al 9 con pasos de 3:", tupla[5:10:3])
print("Slice del 9 al 0 con pasos de -2:", tupla[9:0:-2])
