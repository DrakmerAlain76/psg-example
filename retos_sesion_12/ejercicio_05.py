# Tienes una app para gestionar contactos, cada contacto tiene un nombre y un número de teléfono, 
# si el contacto tiene un número de teléfono válido (11 dígitos incluyendo el código de país) 
# y un nombre valido se guarda en la lista de contactos y muestra el mensaje Contacto guardado, 
# caso contrario se muestra el mensaje de error Datos incorrectos.

nombre = input("Nombre: ").strip()
telefono = input("Teléfono: ").strip()

telefono_valido = telefono.startswith('+') and telefono[1:].isdigit() and len(telefono) == 12
nombre_valido = bool(nombre)

print("Contacto guardado" if telefono_valido and nombre_valido else "Datos incorrectos")
