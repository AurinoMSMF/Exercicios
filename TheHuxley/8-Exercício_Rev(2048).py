nApostas=int(input())
x=0
listaApostas=[]
resultadoLista=[]
while x<nApostas:

    aposta=input()
    apostaAtual=aposta.split(",")
    tamanhoAposta=len(apostaAtual)
    apostaAtual=list(map(int, apostaAtual))
    if(tamanhoAposta>=6 and tamanhoAposta<=10):    
        listaApostas.append(apostaAtual)
    else:
        break
    x+=1

resultado=input()
resultadoOficial=resultado.split(" ")
resultadoOficial=list(map(int, resultadoOficial))

resultadoLista.extend(resultadoOficial)

ganhadores=0

for aposta in listaApostas:
    if(set(resultadoLista).issubset(aposta)):
        ganhadores+=1

print(f"Total de ganhadores: {ganhadores}")
