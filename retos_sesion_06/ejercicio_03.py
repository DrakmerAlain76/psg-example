# 3 Imprime una tabla de verdad para la siguiente sentencia: 
# "Un sistema de seguridad controla el acceso a una habitación, 
# la puerta sólo se abre si se introduce una tarjeta válida o la huella dactilar, 
# pero no ambas al mismo tiempo. Si se introduce la tarjeta y la huella dactilar, 
# la puerta no se abre. ¿Qué operador lógico se puede utilizar?"

# Combinación 1
tarjeta = 0
huella = 0
puerta = (tarjeta and not huella) or (not tarjeta and huella)
print(bool(puerta))

# Combinación 2
tarjeta = 0
huella = 1
puerta = (tarjeta and not huella) or (not tarjeta and huella)
print(bool(puerta))

# Combinación 3
tarjeta = 1
huella = 0
puerta = (tarjeta and not huella) or (not tarjeta and huella)
print(bool(puerta))

# Combinación 4
tarjeta = 1
huella = 1
puerta = (tarjeta and not huella) or (not tarjeta and huella)
print(bool(puerta))

print("operador que se de usar es segundo y tercero")