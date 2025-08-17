# El dueño de una tienda de ropa deportiva ha comprado ropa formal 
# y quiere abrir una nueva tienda que combine ambos estilos. 
# Crea un conjunto con las prendas de ambos tipos con las listas de prendas

# ["Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"]
# ["Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"]

deportiva = ["Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"]
formal = ["Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"]

# Crear conjuntos a partir de las listas
ropa_deportiva = set(deportiva)
ropa_formal = set(formal)

# Unir ambos conjuntos para la nueva tienda
nueva_tienda = ropa_deportiva.union(ropa_formal)

print("Prendas en la nueva tienda:")
print(nueva_tienda)
