#for i in range(1,11):
#    if i % 2 == 0:
#        print(i)
#    else:
#        continue

temperaturas = [25, 32, 18, 40, 22, 12]

#for grau in temperaturas:
#    if grau <= 35:
#        print(f"{grau}°: Por aqui está tudo ok!!")
#    else:
#        print(f"{grau}°:ALERTA!! Suepraquecimento.")

kelvin = []

for i in temperaturas:
    kelvin.append(i + 273.15)

print(kelvin)
