
jogos=[
    ["A","B"],
    ["C","D"],
    ["E","F"],
    ["G","H"],
    ["I","J"],
    ["K","L"],
    ["M","N"],
    ["O","P"]
]

resultadosOitavas=[]
resultadosQuartas=[]
resultadosSemis=[]
resultadoFinal=[]

count=0
count1=0

while True:

    score1,score2=input().split(" ")

    score1=int(score1)
    score2=int(score2)


    if((0<=score1<=20) and (0<=score2<=20)):

        scoresTemp=[]

        scoresTemp.append(score1)
        scoresTemp.append(score2)

        if(count<=7):
            resultadosOitavas.append(scoresTemp)
        if(count>7 and count<=11):
            resultadosQuartas.append(scoresTemp)
        if(count>11 and count<=13):
            resultadosSemis.append(scoresTemp)
        if(count==14):
            resultadoFinal.append(scoresTemp)
        count+=1

    if count==15:
        break



def atualizaChaveCopa(listaJogos,etapaEliminatoria):

    for confronto in listaJogos:
        index=listaJogos.index(confronto)
        if(etapaEliminatoria[index][0]>etapaEliminatoria[index][1]):
                del jogos[index][1]
        else:                
                del jogos[index][0]

    if etapaEliminatoria==resultadoFinal:
        return listaJogos
    else:    
            for i in listaJogos:
                index=listaJogos.index(i)
                if index == 0:
                    team=listaJogos[1][0]
                    partida=team[:]
                    i.extend(partida)
                    del listaJogos[1][0]
                elif index == 2:
                    team=listaJogos[3][0]
                    partida=team[:]
                    i.extend(partida)
                    del listaJogos[3][0]
                elif index == 4:
                    team=listaJogos[5][0]
                    partida=team[:]
                    i.extend(partida)
                    del listaJogos[5][0]
                elif index == 6:
                    team=listaJogos[7][0]
                    partida=team[:]
                    i.extend(partida)
                    del listaJogos[7][0]
            return listaJogos

def removeVazio(lista):
    for i in lista:
        if not i:
            lista.remove(i)
    return lista

oitavas=atualizaChaveCopa(jogos,resultadosOitavas)
oitavas=removeVazio(oitavas)
quartas=atualizaChaveCopa(jogos,resultadosQuartas)
quartas=removeVazio(quartas)
semis=atualizaChaveCopa(jogos,resultadosSemis)
semis=removeVazio(semis)
final=atualizaChaveCopa(jogos,resultadoFinal)
final=removeVazio(final)

print(*final[0])