# 2 Crea un programa que permita construir una canasta de frutas solicitando 
# ingresar frutas por teclado, una por una, y almacenándolas en una lista. 
# El programa debe finalizar cuando se ingrese "salir".

# Solo se permiten las siguientes frutas: 🍅, 🍇, 🍈, 🍉, 🍊, 🍌, 🍍, 🍑

# Si se ingresa una fruta no permitida, el programa debe lanzar una excepción 
# personalizada que indique que la fruta no es válida.

# Lista de frutas permitidas (solo emojis)
frutas_permitidas = ["🍅", "🍇", "🍈", "🍉", "🍊", "🍌", "🍍", "🍑"]

# Excepción personalizada sin __init__
class FrutaNoValidaError(Exception):
    pass

# Canasta de frutas
canasta = []

print("Bienvenido a la canasta de frutas 🍎🥭")
print("Frutas permitidas:", " ".join(frutas_permitidas))
print("Escribe 'salir' para terminar.\n")

while True:
    try:
        entrada = input("Ingrese una fruta (emoji) o 'salir': ").strip()

        if entrada.lower() == "salir":
            print("Saliendo de la canasta...")
            break

        if entrada == "":
            print("No ingresaste nada. Intenta de nuevo.")
            continue

        if entrada not in frutas_permitidas:
            raise FrutaNoValidaError(
                f"La fruta '{entrada}' no está permitida. "
                f"Frutas permitidas: {', '.join(frutas_permitidas)}"
            )

        canasta.append(entrada)
        print(f"✅ {entrada} agregada. Total en la canasta: {len(canasta)}")

    except FrutaNoValidaError as e:
        print(f"❌ Error: {e}")
    except KeyboardInterrupt:
        print("\nInterrupción del usuario. Saliendo...")
        break
    except Exception as e:
        print(f"⚠️ Ocurrió un error inesperado: {e}")

# Resumen final
if canasta:
    from collections import Counter
    conteo = Counter(canasta)
    print("\nResumen final de la canasta:")
    for fruta, cantidad in conteo.items():
        print(f"  {fruta} -> {cantidad}")
    print(f"Total de frutas: {len(canasta)}")
else:
    print("\nLa canasta quedó vacía.")
