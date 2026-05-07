#import os
#moeda = float(input("Quantos reais você quer converter?: "))
#dolar = moeda / 5.21
#print(f"Se você gastar R${moeda}, isso equivale a ${dolar:.2f} dolares!")

nomes = []

itens = int(input("Quantos itens o cliente está pedindo?: "))

pedido = 1

soma = 0

while pedido <= itens:
    print(f"vamos cadastrar o iten {pedido}")
    n_pedido = input(f"Qual o nome do primeiro pedido - {pedido}?: ")

    custo = float(input(f"Qual foi o valor do {n_pedido}?: "))
    
    pedido += 1
    
    soma += custo

    cliente = input("Qual o seu nome?: ")
    nomes.append(cliente)
         

    if cliente in nomes == True:
        print(f"O valor do seu pedido era {custo}, e agora ficou {soma}! Como deseja pagar? ")
    else:
        print(f"O valor foi de {custo}")