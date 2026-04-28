#for i in range(1,11):
#    if i % 2 == 0:
#        print(i)
#    else:
#        continue

#temperaturas = [25, 32, 18, 40, 22, 12]

#for grau in temperaturas:
#    if grau <= 35:
#        print(f"{grau}°: Por aqui está tudo ok!!")
#    else:
#        print(f"{grau}°:ALERTA!! Suepraquecimento.")

#kelvin = []

#for i in temperaturas:
#    kelvin.append(i + 273.15)

#print(kelvin)

#soma = 1
#n = 5
#
#for i in range(1, n + 1):
#    soma *= i
#
#print(f"O resultado foi: {soma}")

volts = [110, 115, 108, 121]

r = 10

potencia = 0 

n = 1

for i in volts:
    potencia = i ** 2 / r
    print(f"a potencia numero {i} é de: {potencia}")
    n += 1