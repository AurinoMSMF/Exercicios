n=int(input())
lista=[]
contador=0
while n-1>=contador:
    adicionar=input()
    lista.append(adicionar)
    contador+=1
for i in range(len(lista)):
    print(lista[i][::-1])