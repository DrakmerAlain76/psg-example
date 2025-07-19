# Una tienda ofrece descuentos a sus clientes, si el cliente tiene una edad mayor a 60 años 
# y tiene una compra mayor a 1000, se le aplica un descuento del 20%, si el cliente tiene una 
# edad entre 18 y 60 años y tiene una compra mayor a 500 se le aplica un descuento del 10%, 
# si no cumple ninguna condición se le aplica un descuento del 2%

edad = int(input("Ingrese su edad: "))
monto = float(input("Ingrese el monto de su compra: "))

if edad > 60 and monto > 1000:
    descuento = 0.20
elif 18 <= edad <= 60 and monto > 500:
    descuento = 0.10
else:
    descuento = 0.02

monto_descuento = monto * descuento
total = monto - monto_descuento

print(f"Descuento aplicado: {descuento * 100}%")
print(f"Monto con descuento: {total:.2f}")
