def cadastro():
    
    info = {"usuario": "Guilherme","Idade": "18", "senha": "1234"}
    
    usuario = str(input("Qual o seu nome?: "))

    idade = int(input("Qual a sua idade?: "))

    senha = input("Digite uma senha segura: ")

    dados = {

    "usuario": usuario, 
    "idade": idade,
    "senha": senha  
    }

    if usuario and idade and senha == None:
        print("Seus dados foram cadastrados com sucesso! ")
    else:
        print("Tente um usuario novo!")


    return usuario, idade, senha, dados, info

    