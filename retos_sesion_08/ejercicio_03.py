# 3 Ingresa una pregunta por teclado y almacena el valor en una tupla
#         Concatena las tupla

# ('¿', ) + pregunta + ('?', )

#     Imprime el resultado concatenado
#     Repite la tupla concatenada 2 veces e imprime el nuevo resultado

# Pedir la pregunta
texto = input("Ingresa una pregunta (sin signos de interrogación): ")

# Crear la tupla con la pregunta
pregunta = (texto,)

# Concatenar los signos de interrogación usando tuplas
pregunta_completa = ('¿',) + pregunta + ('?',)
print("Pregunta concatenada como tupla:", pregunta_completa)

# Repetir la tupla 2 veces
pregunta_repetida = pregunta_completa * 2
print("Pregunta repetida 2 veces como tupla:", pregunta_repetida)
