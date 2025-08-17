# Tienes dos listas: clientes que compraron en la tienda física y clientes que compraron online.

# tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
# tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]

# a. Quiénes compraron en ambos canales.
# b. Quiénes compraron solo en la tienda física.
# c. Quiénes compraron solo online

# Listas de clientes
tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]

# Crear conjuntos a partir de las listas
clientes_fisica = set(tienda_fisica)
clientes_online = set(tienda_online)

# a. Clientes que compraron en ambos canales (intersección)
ambos_canales = clientes_fisica & clientes_online
print("Clientes que compraron en ambos canales:", ambos_canales)

# b. Clientes que compraron solo en la tienda física (diferencia)
solo_fisica = clientes_fisica - clientes_online
print("Clientes que compraron solo en la tienda física:", solo_fisica)

# c. Clientes que compraron solo online (diferencia)
solo_online = clientes_online - clientes_fisica
print("Clientes que compraron solo online:", solo_online)
