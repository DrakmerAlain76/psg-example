#1 Crea una funcion que reciba una lista de calificaciones y devuelva el promedio de las mismas. 
# Las calificaciones son: 50, 75, 80, 91, 70

def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0  
    promedio = sum(calificaciones) / len(calificaciones)
    return promedio

calificaciones = [50, 75, 80, 91, 70]

promedio = calcular_promedio(calificaciones)
print("El promedio de las calificaciones es:", promedio)