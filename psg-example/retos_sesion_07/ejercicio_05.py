# 5 Escribe un programa que reciba una cadena y retorna verdadero o falso si es palindrome sin importar los espacios, mayúsculas o minúsculas 

cadena = "La Ruta Natural"
cadena_limpia = ''.join(cadena.lower().split())
print("Ejemplo: \"La Ruta Natural \" ", cadena_limpia == cadena_limpia[::-1],cadena_limpia[::-1], "->", cadena_limpia[::-1])