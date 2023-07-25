respostas={}
listaDeRespostas=[]
notas=[]
while True:

    dados=input()

    if dados=="*":
        break
    else:
        dados=dados.split()
        nome=dados[0]
        respostasAluno=list(dados[1])
        if len(respostasAluno)>5:
            break
        else:
            respostas.update({nome:respostasAluno})


for nome in respostas:
    listaDeRespostas.append(respostas[nome])


gabarito=list(input())
for respostaUnica in listaDeRespostas:
    nota=0
    for index, respostaLetra in enumerate(respostaUnica):
        if respostaLetra==gabarito[index]:
            nota+=1
    notas.append(nota)
    nota=0
if(not notas):
    print(f"Maior: {0}")
    print(f"Menor: {0}")
    print(f"Media: {0:.2f}")
else:
    maior=max(notas)
    menor=min(notas)
    media=sum(notas)/len(notas)

    print(f"Maior: {maior}")
    print(f"Menor: {menor}")
    print(f"Media: {media:.2f}")