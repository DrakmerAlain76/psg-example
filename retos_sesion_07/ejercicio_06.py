# 6 Agregar 5 Ejemplos con otras funciones no vistas en la sesión
# Utilizar la documentación Métodos de cadenas

texto = "Python es divertido"
print(texto.startswith("Python")) 

archivo = "reporte_final.pdf"
print(archivo.endswith(".pdf"))  

mensaje = "Hola mundo"
print(mensaje.ljust(20, "-"))

frase = "La luna es hermosa esta noche"
print(frase.rjust(40, "."))

numero = "42"
print(numero.zfill(5))
print("7".zfill(3))    
