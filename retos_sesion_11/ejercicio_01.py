# 1 Utiliza un diccionario para almacenar información de un animal marino de un acuario, 
# registra información como especie, habitat, dieta, estado de salud, 
# edad y en un set los nombre de los responsables de su cuidado

print("Información de un animal marino del acuario")

# Diccionario con los datos del animal
animal = {
    "especie": "Tortuga marina",
    "hábitat": "Arrecife de coral",
    "dieta": "Algas y medusas",
    "estado_salud": "Estable",
    "edad": 25
}

# Set con los nombres de los cuidadores
responsables = {"Valeria", "Diego", "Mauricio"}

# Mostrar el diccionario completo
print(animal)
print(type(animal))

# Mostrar el set completo
print(responsables)
print(type(responsables))

# Acceder a datos individuales del diccionario
print(animal["especie"])
print(animal["hábitat"])
print(animal["dieta"])
print(animal["estado_salud"])
print(animal["edad"])
