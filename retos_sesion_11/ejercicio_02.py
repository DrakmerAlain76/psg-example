# 2    Crea un diccionario de alimentos y que animales domésticos lo consumen, por ejemplo

# {"carne" : ["gato", "perro"], "zanahoria" : ["conejo"] }

#     Añade al diccionario 4 alimentos más, usando update(clave=valor)
#     Existe en el diccionario de alimentos la comida 'trigo'?
#     Elimina la comida 'zanahoria' del diccionario de alimentos

print("Diccionario de alimentos y animales domésticos que los consumen")

# Crear el diccionario inicial
alimentos = {"carne": ["gato", "perro"], "zanahoria": ["conejo"]}
print(alimentos)

# Añadir 4 alimentos más usando update(clave=valor)
alimentos.update(pescado=["gato", "perro"])
alimentos.update(semillas=["hamster"])
alimentos.update(leche=["gato"])
alimentos.update(hueso=["perro"])
print(alimentos)

# Verificar si 'trigo' está en el diccionario
existe_trigo = 'trigo' in alimentos
print("¿Existe 'trigo' en el diccionario de alimentos?", existe_trigo)

# Eliminar la comida 'zanahoria'
del alimentos['zanahoria']
print(alimentos)
