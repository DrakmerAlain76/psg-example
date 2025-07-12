# El dueño de una tienda de ropa deportiva ha comprado ropa formal 
# y quiere abrir una nueva tienda que combine ambos estilos. 
# Crea un conjunto con las prendas de ambos tipos con las listas de prendas

# ["Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"]
# ["Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"]

ropa_deportiva = {"Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"}
ropa_formal = {"Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"}

nueva_tienda = set(ropa_deportiva) | set(ropa_formal)
nueva_tienda = set(ropa_deportiva).union(ropa_formal)
print(nueva_tienda)
