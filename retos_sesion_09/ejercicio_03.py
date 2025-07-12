# Crear una lista de personas con 10 nombres de personas

#    Obtener una sub lista de 5 a 9 con saltos de 2 en 2
#    Buscar si existe el nombre "José" en la lista original
#    Ordenar la sub lista alfabéticamente a-z
#    Ordenar la lista original alfabéticamente descendente z-a

personas = ["Ana", "Luis", "Carlos", "María", "José", "Elena", "Pedro", "Lucía", "Marta", "Diego"]

# 1. Obtener una sub lista de 5 a 9 con saltos de 2 en 2
sublista = personas[5:10:2]
print("Sublista (índices 5 al 9, salto de 2):", sublista)

# 2. Buscar si existe el nombre "José" en la lista original
existe_jose = "José" in personas
print("¿Está 'José' en la lista?:", existe_jose)

# 3. Ordenar la sub lista alfabéticamente a-z
personas.sort()
print("Sublista ordenada A-Z:", personas)

# 4. Ordenar la lista original alfabéticamente descendente z-a
personas.sort(reverse=True)
print("Lista original ordenada Z-A:", personas)
