def separaElementos(lista):
    copLista=[]
    numError=0
    for e in lista:
        e=int(e)
        copLista.append(e)
    for e in copLista:
        if e>7 or e<1:
            numError=1
            break
        else:
            numError=0
    if numError==1:
        return numError
    else:
        return copLista

def analisaChute(elementosSenha, chutes):
    pontuacaoChute = [0, 0]

    elementosRestantesSenha=[]
    elementosRestantesChute=[]


    for index, elemento in enumerate(elementosSenha):
        if elemento == chutes[index]:
            pontuacaoChute[0] += 1
        else:
            elementosRestantesSenha.append(elemento)
            elementosRestantesChute.append(chutes[index])

    for elemento in elementosRestantesChute:
        if elemento in elementosRestantesSenha:
            pontuacaoChute[1] += 1
            elementosRestantesSenha.remove(elemento)

    return pontuacaoChute

numeroJogos=int(input())

elementosSenha=[]
chutes=[]
x=0
while x<numeroJogos:
    
    numCaracteresSenha=int(input())

    if numCaracteresSenha>0 and numCaracteresSenha<8:

        senha=list(input())
        senha=separaElementos(senha)
        if(type(senha)==list):    
            elementosSenha.extend(senha)
            if (len(elementosSenha)==numCaracteresSenha):

                correto=0
            
                while correto!=1:
                    chute=list(input())
                    chute=separaElementos(chute)
                    if(type(chute)!=int):
                        chutes.extend(chute)
                        pontuacao=analisaChute(elementosSenha,chutes)
                        if pontuacao[0] == len(elementosSenha) and pontuacao[1]==0:   
                            print("(%d,%d)"%(pontuacao[0], pontuacao[1]))
                            correto=1
                            chutes=[]
                            break
                        else:
                            print("(%d,%d)"%(pontuacao[0], pontuacao[1]))
                            chutes=[]
                    else:
                        break
            else:
                break
            x+=1
        else:
            break
    
    else:
        break
    elementosSenha=[]