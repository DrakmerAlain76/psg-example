#3  Jhon colecciona autos a escala 1:64, tiene los siguientes autos
# {'Ferrari', 'Lamborghini', 'Porsche', 'Bugatti', 'McLaren'}
# Jess tambien colecciona autos a escala 1:64, tiene los siguientes autos
# {'Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Chevrolet'}
# ¿Que autos tienen en común ambos coleccionistas?, 
# ¿Cuáles son los autos en común?


jhon_autos = {'Ferrari', 'Lamborghini', 'Porsche', 'Bugatti', 'McLaren'}

jess_autos = {'Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Chevrolet'}

autos_en_comun = jhon_autos & jess_autos

print("Autos en común:", autos_en_comun)
