#import random
#import os 
#
#def clean():
#    os.system('cls')
#
#numero = random.randint(1, 10)
#
#while True: 
#
#    adivinha = int(input("Adivinha o numero que eu estou pensando!: "))
#
#    if adivinha < numero:
#        print("O numero é maior")
#        
#    elif adivinha == numero:
#        print("Parabéns! Você acertou")
#        print(f"O numero era: {numero}")
#        break
#        
#    else:
#        print("O número é menor")

#nome = input("Qual o seu nome?: ")
#print(nome)

semestre = 1 

while semestre <= 2:
   
    cp1 = int(input("Qual a nota do seu primeiro CheckPoint?: "))
    cp2 = int(input("Qual a nota do seu segundo CheckPoint?: "))
    cp3 = int(input("Qual a nota do seu terceiro CheckPoint?: "))
    sp1 = int(input("Qual foi a sua nota na Sprint1?: "))
    sp2 = int(input("Qual foi a sua nota na Sprint2?: "))
    gs = int(input("Qual foi a sua nota na Global Solution?: "))   

    menor_cp = cp1

    if cp1 <= cp2 and cp1 <= cp3:
        menor_cp = cp1
    elif cp2 <= cp1 and cp2 <= cp3:
        menor_cp = cp2
    else:
        menor_cp = cp3
    
    print(f"A seu menor CheckPoint foi {menor_cp}")

    media = ((cp1 + cp2 + cp3 - menor_cp + sp1 + sp2) / 4) * 0.4 + gs * 0.6
    
    print(f"A sua média do bimestre {semestre} foi: {media:.1f}")
    
    semestre += 1


