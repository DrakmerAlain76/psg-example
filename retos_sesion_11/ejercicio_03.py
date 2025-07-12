# 3 
#     Crea un diccionario con la siguiente tupla de especies animales

# (('canino', '🐶') , ('felino','🐱') , ('aves',['🐦','🦅']))

#     Del diccionario obtén y elimina el valor de la clave 'aves'
#     Modifica el valor de la clave 'felino' por '🐈'
#     Cambia la clave canino por caninos y su valor por ['🐶','🐕']

# Crear diccionario a partir de la tupla
tupla = (('canino', '🐶'), ('felino', '🐱'), ('aves', ['🐦', '🦅']))
diccionario = dict(tupla)
print("Diccionario inicial:")
print(diccionario)

# Obtener y eliminar el valor de la clave 'aves'
aves = diccionario.pop('aves')
print("\nValor eliminado de la clave 'aves':", aves)
print("Diccionario después de eliminar 'aves':")
print(diccionario)

# Modificar el valor de la clave 'felino' por '🐈'
diccionario['felino'] = '🐈'
print("\nDiccionario después de modificar 'felino':")
print(diccionario)

# Cambiar la clave 'canino' por 'caninos' y su valor por ['🐶','🐕']
diccionario['caninos'] = ['🐶', '🐕']  # Nuevo par clave-valor
del diccionario['canino']  # Eliminar clave antigua
print("\nDiccionario final después de cambiar 'canino' a 'caninos':")
print(diccionario)
