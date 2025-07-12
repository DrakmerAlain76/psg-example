#6 ¿El cubo de 300 se encuentra en el siguiente rango? [N > 0 & N < 27_000_000]

cubo = 300 ** 3  # Elevamos al cubo
en_rango = cubo > 0 and cubo < 27_000_000  # Verificamos si está dentro del rango
print("¿El cubo de 300 está en el rango (0, 27_000_000)?", en_rango)
