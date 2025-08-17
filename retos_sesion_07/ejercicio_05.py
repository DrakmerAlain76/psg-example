# 5 Escribe un programa que reciba una cadena y retorna verdadero o falso si es palindrome sin importar los espacios, mayúsculas o minúsculas 

cadena = input("Ingresa una cadena: ")

cadena_limpia = ''.join(cadena.lower().split())

es_palindrome = cadena_limpia == cadena_limpia[::-1]

print(f"Cadena original: {cadena}")
print(f"Cadena limpia: {cadena_limpia}")
print(f"Inversa: {cadena_limpia[::-1]}")
print(f"¿Es palindrome? {es_palindrome}")
