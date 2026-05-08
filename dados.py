def cadastro():
    
    
    usuario = str(input("Qual o seu nome?: "))

    idade = int(input("Qual a sua idade?: "))

    senha = input("Digite uma senha segura: ")

    dados = {

    "usuario": usuario, 
    "idade": idade,
    "senha": senha  
    }


    if usuario and idade and senha:
        print("Seus dados foram cadastrados com sucesso! ")
    else:
        print("Tente um usuario novo!")


    return usuario, idade, senha, dados

    