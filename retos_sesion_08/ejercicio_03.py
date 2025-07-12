# 3 Ingresa una pregunta por teclado y almacena el valor en una tupla
#         Concatena las tupla

# ('¿', ) + pregunta + ('?', )

#     Imprime el resultado concatenado
#     Repite la tupla concatenada 2 veces e imprime el nuevo resultado

texto = input("Ingresa una pregunta (sin signos de interrogación): ")

pregunta = tuple([texto])  # Creamos una tupla con la pregunta

# Concatenamos con signos de interrogación
pregunta_completa = ('¿',) + pregunta + ('?',)

# Unimos todos los elementos en una sola cadena
cadena_final = ''.join(pregunta_completa)
print("Pregunta unida:", cadena_final)

# Repetimos la tupla y volvemos a unir
cadena_repetida = ''.join(pregunta_completa * 2)
print("Pregunta repetida 2 veces:", cadena_repetida)
