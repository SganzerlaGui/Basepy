notas_alunos = {}

def media_dos_alunos():
    input("1 - Cadastrar Notas\n",
          "2 - Mostrar Notas\n"
          "3 - Meddia dos alunos\n"
          "4 - Sair\n")
    
    opcao = int(input("Qual opção você deseja selecionar?: "))

    return opcao

def cadastrar_notas():
    
    alunos = int(input("Quantos alunos você deseja cadastrar a nota?: "))

    for notas_alunos in alunos:
        
        cp1 = float(input("qual foi a sua nota do Checkpoint 1?: "))
   
        cp2 = float(input("Qual foi a sua nota do Checkpoint 2?: "))
    
        cp3 = float(input("Qual foi a sua nota do Checkpoint 3?: "))
    
        if cp1 <= cp2 and cp1 <= cp3:
        
            print(f"A menor nota foi a {float(cp1):.2f}, ela será descontada!")
            menor_nota = cp1
    
        elif  cp2 <= cp1 and cp2 <= cp3:
            print(f"A menor nota foi a {float(cp2):.2f}, ela será descontada!")
            menor_nota = cp2

        elif cp3 <= cp1 and cp3 <= cp2:
            print(f"A menor nota foi a {float(cp3):.2f}, ela será descontada!")
            menor_nota = cp3

        else:
            print("Não foi possivel entender oque você escreveu!")

        menor_cp = menor_nota

        sp1 = float(input("Qual foi a sua nota do Sprint 1 ?: "))

        sp2 = float(input("Qual foi a sua nota do Sprint 2?: "))

        gs = float(input("Qual foi a sua nota do Global Solution?: "))

        media = (((cp1 + cp2 + cp3 - menor_cp + sp1 + sp2) / 4) * 0.4 + gs * 0.6).append(notas_alunos)

        return media

        

