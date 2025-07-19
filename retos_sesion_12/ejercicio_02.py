
#2 Tienes una app para gestionar tareas de 4 usuarios, para acceder los usuarios 
# deben iniciar sesión con un nombre de usuario y una contraseña introducidos por teclado.
# Define los siguientes usuarios y contraseñas utilizando la estructura de datos mas adecuada.
# Usuario: admin, Contraseña: admin123
# Usuario: user1, Contraseña: user123
# Usuario: user2, Contraseña: user123
# Usuario: user3, Contraseña: user123
# Diccionario de usuarios y contraseñas

usuarios = {
    "admin": "admin123",
    "user1": "user123",
    "user2": "user123",
    "user3": "user123"
}

usuario = input("Nombre de usuario: ")
contrasena = input("Contraseña: ")

acceso = usuario in usuarios and usuarios[usuario] == contrasena

print("Acceso Aprobado" if acceso else "Acceso Denegado")
