
p=input()

def inteiros(lista):
    n=["0","1","2","3","4","5","6","7","8","9"]
    binary=True
    for j in lista:
        a=list(n)
        for k in a:
            k=int(k)            
            if j == n[k]:
                j=int(j)
                binary=False
    return binary

def substitui(lista):
    subs=0
    for i in lista:
                
                if(i=="a" or i=="A"):
                    index=lista.index(i)
                    lista[index]="@"
                    subs+=1
                elif(i=="e" or i=="E"):
                    index=lista.index(i)
                    lista[index]="3"
                    subs+=1
                elif(i=="i" or i=="I"):
                    index=lista.index(i)
                    lista[index]="1"
                    subs+=1
                elif(i=="o" or i=="O"):
                    index=lista.index(i)
                    lista[index]="0"
                    subs+=1
                elif(i=="t" or i=="T"):
                    index=lista.index(i)
                    lista[index]="7"
                    subs+=1
                elif(i=="s" or i=="S"):
                    index=lista.index(i)
                    lista[index]="5"
                    subs+=1

    reverseList=reversed(lista)
        
    leet="".join(reverseList)
        
    print(leet)
    print(subs)

if(p=="" or p==" "):
    print("vazio")
    print(0)
else:
    p=list(p)


    j=inteiros(p)

    if j == False:
        print("numeros")
        print(0)

    elif j==True:

        substitui(p)