# 3 Imprime una tabla de verdad para la siguiente sentencia: 
# "Un sistema de seguridad controla el acceso a una habitación, 
# la puerta sólo se abre si se introduce una tarjeta válida o la huella dactilar, 
# pero no ambas al mismo tiempo. Si se introduce la tarjeta y la huella dactilar, 
# la puerta no se abre. ¿Qué operador lógico se puede utilizar?"
print("Tabla de verdad - Acceso con tarjeta XOR huella (solo uno de los dos):")
print("Tarjeta\tHuella\tPuerta")

# Combinación 1
tarjeta = 0
huella = 0
puerta = (tarjeta and not huella) or (not tarjeta and huella)
print(f"{tarjeta}\t{huella}\t{puerta}")

# Combinación 2
tarjeta = 0
huella = 1
puerta = (tarjeta and not huella) or (not tarjeta and huella)
print(f"{tarjeta}\t{huella}\t{puerta}")

# Combinación 3
tarjeta = 1
huella = 0
puerta = (tarjeta and not huella) or (not tarjeta and huella)
print(f"{tarjeta}\t{huella}\t{puerta}")

# Combinación 4
tarjeta = 1
huella = 1
puerta = (tarjeta and not huella) or (not tarjeta and huella)
print(f"{tarjeta}\t{huella}\t{puerta}")

print("\nEl operador lógico que se puede utilizar es el XOR (^).")
