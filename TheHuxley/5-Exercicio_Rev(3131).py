
def remover_especiais(palavra):
    palavra=list(palavra)
    for i in palavra:
        #. " ( * $ # :
        #i =="*" or i=="$" or i=="(" or i=="." or i ==":" or i == '\"' or i=="#"
        if (i =="*") or (i=="$") or (i=="(") or (i==".") or (i ==":") or (i == '"') or (i=="#"):
            #palavra.remove(i)
    #LEMBRE DE UNIR OS DOIS FOR E CONTINUAR OS AJUSTES A PARTIR DA?!!
            index=palavra.index(i)
            palavra[index]="/"
    palavra="".join(palavra)
    return palavra

palavrasEntrada=[]

palavrasSeparadas=[]

while True:

    entrada=(input().lower())
    if entrada=="-1":
        break
    elif entrada!="-1":
        palavrasEntrada.append(entrada)



#Cria um loop aninhado dentro destas linhas para remover os espa?os e torn?-las um corpode texto

for i in palavrasEntrada:
    if " " in i:
        palavrasSeparadas.extend(i.split(" "))
    else:
        palavrasSeparadas.append(i)

palavrasTratadas=[]

for i in palavrasSeparadas:
        palavraLimpa=remover_especiais(i)
        palavrasTratadas.append(palavraLimpa)

palavrasTratadas.sort()

palavrasRepetidas={}

corrigidas=[]

for j in palavrasTratadas:
    if "/" in j:
        correcoes=j.split("/")
        corrigidas.extend(correcoes)
        palavrasTratadas.remove(j)
        palavrasTratadas.extend(correcoes)

for j in palavrasTratadas:
    if "/" in j:
        correcoes=j.split("/")
        corrigidas.extend(correcoes)
        palavrasTratadas.remove(j)
        palavrasTratadas.extend(correcoes)

palavrasTratadas.sort()

for i in palavrasTratadas:
    repeticoes=palavrasTratadas.count(i)
    palavrasRepetidas.update({i : repeticoes})

branco=palavrasRepetidas.pop("")

for x, y in palavrasRepetidas.items():
  print(x, y) 
