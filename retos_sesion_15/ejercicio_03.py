# Crea un programa que simule el funcionamiento de un cajero automático solicitando al usuario un monto a retirar. 
# Si el monto ingresado es mayor al saldo disponible, el programa debe lanzar una excepción 
# personalizada que indique que no hay fondos suficientes. Además, si el monto ingresado es mayor a 1000,
# debe lanzarse una excepción genérica que advierta que el monto excede el límite permitido por transacción.

# Excepción personalizada
class FondosInsuficientesError(Exception):
    pass

# Saldo inicial
saldo = 800

print("💰 Bienvenido al cajero automático")
print(f"Saldo disponible: {saldo} Bs\n")

try:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto > saldo:
        raise FondosInsuficientesError("Fondos insuficientes para realizar la transacción.")
    
    if monto > 1000:
        raise Exception("El monto excede el límite permitido por transacción (1000 Bs).")
    
    saldo -= monto
    print(f"✅ Retiro exitoso. Nuevo saldo: {saldo} Bs")

except FondosInsuficientesError as e:
    print(f"❌ Error: {e}")
except Exception as e:
    print(f"⚠️ Error: {e}")

