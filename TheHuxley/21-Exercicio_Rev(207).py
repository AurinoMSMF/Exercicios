def viraInteiro(lista):
    listaInteiros=[]
    for e in lista:
        e=int(e)
        listaInteiros.append(e)
    return listaInteiros
dados=input().split()
numeroDeCompetidores=int(dados[0])
numeroDeVoltas=int(dados[1])
x=0
tempos=[]
while x<numeroDeCompetidores:
    tempoCadaVolta=input().split()
    tempoCorrigido=viraInteiro(tempoCadaVolta)
    tempos.append(tempoCorrigido)
    x+=1
melhorTempo=0
campeao=None
melhoresTempos=[]
for index,tempoIndividual in enumerate(tempos):
    melhoresTempos.append(sum(tempoIndividual))
print(melhoresTempos.index(min(melhoresTempos))+1)
