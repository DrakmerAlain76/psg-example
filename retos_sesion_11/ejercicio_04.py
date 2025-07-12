#     Gestión de hábitats en peligro: Crea un diccionario que asocie especies animales en peligro de extinción con información sobre sus hábitats amenazados, lo que permite priorizar la protección de áreas críticas para la supervivencia de estas especies

# {"polo norte" : {
#     "especies": {"oso polar", "morsa", "ballena"}
#   }, "amazonas" : {
#     "especies": {"tigre", "mono", "guacamayo"}
#   }
# }

#     Añade al diccionario 2 habitats más usando update() con 2 especies cada uno
#     Existe en el diccionario el habitat 'amazonas'?
#     Añade al amazonas la especie 'anaconda'
# Diccionario inicial con hábitats y sus especies en peligro

habitats = {
    "polo norte": {
        "especies": {"oso polar", "morsa", "ballena"}
    },
    "amazonas": {
        "especies": {"tigre", "mono", "guacamayo"}
    }
}

print("Diccionario inicial:")
print(habitats)

# Añadir 2 hábitats más con 2 especies cada uno usando update()
habitats.update({
    "sabana africana": {
        "especies": {"elefante", "león"}
    },
    "bosque boreal": {
        "especies": {"lobo", "búho"}
    }
})

print("\nDiccionario después de añadir dos hábitats:")
print(habitats)

# Verificar si 'amazonas' existe en el diccionario
existe_amazonas = "amazonas" in habitats
print("\n¿Existe el hábitat 'amazonas'?", existe_amazonas)

# Añadir la especie 'anaconda' al hábitat 'amazonas'
habitats["amazonas"]["especies"].add("anaconda")

print("\nDiccionario después de añadir 'anaconda' al 'amazonas':")
print(habitats)

