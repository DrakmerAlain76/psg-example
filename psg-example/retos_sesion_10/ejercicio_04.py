# Jane y Jhon llevan saliendo juntos por 4 semanas, cada vez que salen van a comer a un candy bar. 
# Quieren saber que tan compatibles son viendo cuantos platos de comida tienen en común. 
# A continuación tienes los postres que han ido pidiendo en cada salida:

# Jane: Lemon Pie, Brownie, Tarta de Manzana,
#       Helado de Chocolate, Flan
# Jhon: Carrot Cake, Croissant de Chocolate,
#       Lemon Pie, Tarta de Manzana, Pudding
# 
# Si la cantidad de postres que tienen en común es mayor al 50% 
# entonces son compatibles,
# de lo contrario quieren replantear su relación

jane = {"Lemon Pie", "Brownie", "Tarta de Manzana", "Helado de Chocolate", "Flan"}
jhon = {"Carrot Cake", "Croissant de Chocolate", "Lemon Pie", "Tarta de Manzana", "Pudding"}

en_comun = jane & jhon
total_postres = jane | jhon
porcentaje_comun = len(en_comun) / len(total_postres)

mensaje_compatible = "¡Son compatibles! 💕"
mensaje_no_compatible = "Tal vez deban replantear su relación 💔"

mensaje = (porcentaje_comun > 0.5) * mensaje_compatible + (porcentaje_comun <= 0.5) * mensaje_no_compatible

print(mensaje)
print("Postres en común:", en_comun)
print("Compatibilidad:", round(porcentaje_comun * 100, 2), "%")