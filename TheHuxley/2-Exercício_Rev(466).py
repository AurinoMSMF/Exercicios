"""
*Descrição:

Ester está programando suas férias e decidiu viajar gastando no máximo R$ 300 de passagens (ida e volta). Para usar bem seu dinheiro, ela quer ir para a cidade mais longe possível sem extrapolar seu orçamento. Escreva um programa que receba como entrada o nome, a distância (em quilômetros) e o valor da passagem (só ida) de várias cidades, até que ela informe a cidade FIM, e exiba o nome do melhor destino para ela.

Obs: Considere que as passagens de ida e de volta tenham o mesmo valor

*Formato de entrada:

Um String (que pode estar escrito de qualquer forma), um inteiro (km) e um real para cada cidade
Para encerrar a entrada, será informado o String FIM (escrito de qualquer forma) como nome da cidade

*Formato de saída:

Um String com as letras todas maiúsculas
Se nenhuma cidade for informada, deverá ser exibida a mensagem SEM DESTINO

"""

#Preço maximo das passagens: 300
cidades=[]
distancias=[]
valores=[]
valoresInvalidos=[]
while True:
    
    cidade = str(input()).upper()
    if(cidade == "" or (" " in cidade)):
        print("SEM DESTINO")
        break
    elif(cidade=="FIM"):
        break
    else:
        cidades.append(cidade)
        distancia=int(input())
        if((distancia == True) or distancia<0):
            break
        else:
            distancias.append(distancia)
            passagemIda=float(input())
            if(passagemIda<0):
                break
            else:
                valor=passagemIda*2
                if valor>300 or valor<0:
                    valoresInvalidos.append(valor)
                    distancias.remove(distancia)
                    cidades.remove(cidade)
                else:
                    valores.append(valor)

tamanhoListaCidades=len(cidades)
diferencas=[]

for i in range(0,tamanhoListaCidades):
    diferenca=distancias[i]-valores[i]
    if(diferenca<0):
        diferenca*=-1
    diferencas.append(diferenca)

maior=0

for j in range(tamanhoListaCidades):
    if(j==0):
        maior=diferencas[j]
    else:
        if(diferencas[j]>maior):
            maior=diferencas[j]

melhorDestino=""
indices=[]
melhoresValores=[]
for indice, valor in enumerate(diferencas):
    if(valor==maior):
        indices.append(indice)
        if(valores[indice]):
            melhoresValores.append(valores[indice])
        for i,v in enumerate(melhoresValores):
            if(v==max(melhoresValores)):
                melhorDestino=cidades[i]

if(melhorDestino==""):
    print("SEM DESTINO")
else:
    print(melhorDestino)