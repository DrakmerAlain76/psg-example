# 1 Utiliza un diccionario para almacenar información de un animal marino de un acuario, 
# registra información como especie, habitat, dieta, estado de salud, 
# edad y en un set los nombre de los responsables de su cuidado

# Lista de animales marinos en el acuario
acuario = [
    {
        "especie": "Delfín nariz de botella",
        "hábitat": "Piscina principal de mamíferos marinos",
        "dieta": "Peces pequeños, calamares y crustáceos",
        "estado_de_salud": "Saludable",
        "edad": 8,
        "responsables": {"Ana", "Carlos", "María"}
    },
    {
        "especie": "Tiburón martillo",
        "hábitat": "Tanque de grandes depredadores",
        "dieta": "Peces, rayas y cefalópodos",
        "estado_de_salud": "En observación",
        "edad": 15,
        "responsables": {"Luis", "Carolina"}
    },
    {
        "especie": "Tortuga marina verde",
        "hábitat": "Laguna costera artificial",
        "dieta": "Algas y pastos marinos",
        "estado_de_salud": "Recuperación",
        "edad": 80,
        "responsables": {"Sofía", "Pedro", "María"}
    }
]

print("Información del acuario:\n")

# Salida
print(f"Especie: {acuario[0]['especie']}")
print(f"Hábitat: {acuario[0]['hábitat']}")
print(f"Dieta: {acuario[0]['dieta']}")
print(f"Estado de salud: {acuario[0]['estado_de_salud']}")
print(f"Edad: {acuario[0]['edad']} años")
print(f"Responsables: {', '.join(acuario[0]['responsables'])}\n")

print(f"Especie: {acuario[1]['especie']}")
print(f"Hábitat: {acuario[1]['hábitat']}")
print(f"Dieta: {acuario[1]['dieta']}")
print(f"Estado de salud: {acuario[1]['estado_de_salud']}")
print(f"Edad: {acuario[1]['edad']} años")
print(f"Responsables: {', '.join(acuario[1]['responsables'])}\n")

print(f"Especie: {acuario[2]['especie']}")
print(f"Hábitat: {acuario[2]['hábitat']}")
print(f"Dieta: {acuario[2]['dieta']}")
print(f"Estado de salud: {acuario[2]['estado_de_salud']}")
print(f"Edad: {acuario[2]['edad']} años")
print(f"Responsables: {', '.join(acuario[2]['responsables'])}\n")
