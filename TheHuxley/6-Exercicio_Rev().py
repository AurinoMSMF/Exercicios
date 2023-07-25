
def checaDirecao(lista):

    for i in lista:
        if(lista[-1]=="e"):
            return "e"
        if(lista[-1]=="d"):
            return "d"
        if(lista[-1]=="b"):
            return "b"
        if(lista[-1]=="c"):
            return "c"            

mapaCidade=[[0 for coluna in range(4)] for linha in range(4)
    
    #0 1 2 3 
    #[0,0,0,0], #0
    #[0,0,0,0], #1
    #[0,0,0,0], #2
    #[0,0,0,0]  #3

]

cont=0

direcoes=[]

direcaoAnterior=checaDirecao(direcoes)

while True:

    passo=input().split(" ")
    
    if(passo and (not passo==" ")):

        if passo=="d" or passo=="e":

            direcoes.append(passo)

            if passo=="e" and cont==0:
                break
            elif(passo=="e"):
                for linha in mapaCidade:
                    for coluna in linha:
                        if coluna==linha[0]:#se a coluna for igual primeira linha

                            if direcaoAnterior == ""

                            mapaCidade[0][]+=1

                        elif coluna==linha[1]:#segunda linha

                            mapaCidade[1][]+=1

                        elif coluna==linha[2]:#terceira linha



                        elif coluna==linha[3]:#quarta linha
                        
                            

        cont+=1