# 5    Eres NOE y tienes que guardar dos animales de cada especie en un arca, crea un diccionario con las especies

# {"🐶" : 2, "🐱" : 2, "🐯" : 2, "🐵" : 2, "🦄" : 0, "🦒" : 1}

#     Añade al arca 3 especies más usando update()
#     Toma lista de los animales en el arca iterando el diccionario
#     Existe en el arca la especie 'dragon' 🐲?
#     Elimina la especie unicornio del arca
#     Modifica el valor de la especie jirafa por 2
#     Vacía el arca después del diluvio

# Crear el diccionario inicial
arca = {"🐶": 2, "🐱": 2, "🐯": 2, "🐵": 2, "🦄": 0, "🦒": 1}
print("Arca inicial:")
print(arca)

# Añadir 3 especies más usando update()
arca.update({"🐰": 2, "🐸": 2, "🐢": 2})
print("\nArca después de añadir 3 especies:")
print(arca)

# Tomar lista de los animales en el arca iterando el diccionario
# Sin usar for, se puede usar list() con keys() o items()
lista_animales = list(arca.items())
print("\nLista de animales en el arca (especie y cantidad):")
print(lista_animales)

# Verificar si 'dragon' 🐲 está en el arca
existe_dragon = '🐲' in arca
print("\n¿Existe el dragón 🐲 en el arca?", existe_dragon)

# Eliminar la especie unicornio 🦄 del arca
del arca['🦄']
print("\nArca después de eliminar el unicornio 🦄:")
print(arca)

# Modificar el valor de la especie jirafa 🦒 por 2
arca['🦒'] = 2
print("\nArca después de modificar la jirafa 🦒 a 2:")
print(arca)

# Vaciar el arca después del diluvio
arca.clear()
print("\nArca después del diluvio (vacía):")
print(arca)
