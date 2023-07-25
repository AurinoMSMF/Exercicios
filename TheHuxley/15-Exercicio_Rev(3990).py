def transformaEmFloat(lista):
    lista[1]=lista[1].replace(',' , '.')
    lista[1]=float(lista[1])
    return lista
def corrigeData(lista):
    for i in range(len(lista)):
        data = lista[i]
        ano = data[:4]
        mes = data[5:]
        lista[i] = mes + "-" + ano
    return lista
def maiorEMenor(lista):
    menor_elemento=lista[0]
    maior_elemento=lista[0]
    for elemento in lista:
        if(elemento<menor_elemento):
            menor_elemento=elemento
        if(elemento>maior_elemento):
            maior_elemento=elemento
    indiceMenor=lista.index(menor_elemento)
    indiceMaior=lista.index(maior_elemento)
    return menor_elemento,maior_elemento,indiceMenor,indiceMaior
datas=[]
ipcas=[]
datas_ipcas=[]
while True:
    data_ipca=input()
    if data_ipca=="*":
        break
    datas_ipcas=data_ipca.split(" ")
    transformaEmFloat(datas_ipcas)
    datas.append(datas_ipcas[0])
    ipcas.append(datas_ipcas[1])
datasCorrigidas=corrigeData(datas)
menor_e_maior=maiorEMenor(ipcas)
menorIpca,maiorIpca,indiceMenor,indiceMaior=menor_e_maior
print(f"Menor: {menorIpca} ({datas[indiceMenor]})")
print(f"Maior: {maiorIpca} ({datas[indiceMaior]})")
mediaIpcas=sum(ipcas)/len(ipcas)
print(f"Media: {mediaIpcas:.2f}")