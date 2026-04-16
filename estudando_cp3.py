import random
import os 

def clean():
    os.system('cls')

numero = random.randint(1, 10)

while True: 

    adivinha = int(input("Adivinha o numero que eu estou pensando!: "))

    if adivinha < numero:
        print("O numero é maior")
        
    elif adivinha == numero:
        print("Parabéns! Você acertou")
        print(f"O numero era: {numero}")
        break
        
    else:
        print("O número é menor")

