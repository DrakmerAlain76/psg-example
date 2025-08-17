#Escribe un programa en Python que convierta 1000000 de segundos en semanas, días, horas, minutos y segundos
#Ejemplo:
#788521 segundos = 9 días 3 horas 2 minutos 1 segundo
# Total de segundos
total_segundos = 1000000

# Cálculos
semanas = total_segundos // (7 * 24 * 60 * 60)
resto = total_segundos % (7 * 24 * 60 * 60)

días = resto // (24 * 60 * 60)
resto %= (24 * 60 * 60)

horas = resto // (60 * 60)
resto %= (60 * 60)

minutos = resto // 60
segundos = resto % 60

# Mostrar el resultado
print(total_segundos, "segundos =",semanas,"semanas", días, "días", horas,"horas", minutos, "minutos",segundos, "segundos")
