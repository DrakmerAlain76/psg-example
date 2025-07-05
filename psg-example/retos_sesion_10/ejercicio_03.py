# Tienes dos listas: clientes que compraron en la tienda física y clientes que compraron online.

# tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
# tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]

# a. Quiénes compraron en ambos canales.
# b. Quiénes compraron solo en la tienda física.
# c. Quiénes compraron solo online

tienda_fisica = {"Ana", "Luis", "Pedro", "María", "Juan"}
tienda_online = {"Pedro", "María", "Ana", "Carlos", "Laura"}

ambos = tienda_fisica & tienda_online

solo_fisica = tienda_fisica - tienda_online

solo_online = tienda_online - tienda_fisica

print("a. Ambos:", ambos)
print("b. Solo tienda física:", solo_fisica)
print("c. Solo online:", solo_online)


