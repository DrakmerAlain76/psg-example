# Una dulcería tiene 2 listas una con los productos y otra con los precios

#    Agregar 2 productos nuevos al final de las listas
#    Eliminar el producto con el nombre "Bon Bon Bum" de las listas
#    ¿Cuánto cuesta el producto "Oreo" y "Chizitos"?
#    ¿Cuál es el producto más caro y el más barato?
#    ¿Cuántos productos tienes en total?
#    ¿Cuanto cuestan todos los productos?
#    Ordena los productos y precios del más barato al más caro
#    Eliminar todos los productos de las listas

# Listas iniciales
productos = ["Oreo", "Chizitos", "Bon Bon Bum", "Snickers", "Galleta Animalitos"]
precios = [2.5, 1.2, 0.8, 3.0, 1.5]

# 1. Agregar 2 productos nuevos al final
productos.append("Milka")
precios.append(4.0)

productos.append("Mentas")
precios.append(0.5)

# 2. Eliminar "Bon Bon Bum" de ambas listas (sin if)
indice_bonbon = productos.index("Bon Bon Bum")
productos.pop(indice_bonbon)
precios.pop(indice_bonbon)

# 3. Precios de "Oreo" y "Chizitos"
precio_oreo = precios[productos.index("Oreo")]
precio_chizitos = precios[productos.index("Chizitos")]
print("Precio de Oreo:", precio_oreo)
print("Precio de Chizitos:", precio_chizitos)

# 4. Producto más caro y más barato
max_precio = max(precios)
min_precio = min(precios)

producto_caro = productos[precios.index(max_precio)]
producto_barato = productos[precios.index(min_precio)]
print("Más caro:", producto_caro, "-", max_precio)
print("Más barato:", producto_barato, "-", min_precio)

# 5. Cantidad total de productos
print("Total de productos:", len(productos))

# 6. Costo total
print("Costo total:", sum(precios))

# 7. Ordenar productos y precios del más barato al más caro
orden = sorted(zip(precios, productos))
precios = [orden[0][0], orden[1][0], orden[2][0], orden[3][0], orden[4][0], orden[5][0]]
productos = [orden[0][1], orden[1][1], orden[2][1], orden[3][1], orden[4][1], orden[5][1]]

print("Productos ordenados por precio ascendente:", productos)
print("Precios ordenados:", precios)

# 8. Eliminar todos los productos
productos.clear()
precios.clear()

print("Listas vacías:", productos, precios)
