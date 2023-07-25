a,b,c=input().split(" ")

a=int(a)
b=int(b)
c=int(c)

lados=[]

lados.append(a)
lados.append(b)
lados.append(c)

x=0

def verificaTriangulo(listaDeLados):

    a=listaDeLados[0]
    b=listaDeLados[1]
    c=listaDeLados[2]

    if not(a+b>c and b+c>a and c+b>a and a+c>b):
        print("nao eh triangulo")
    elif all(elemento == listaDeLados[0] for elemento in listaDeLados):
        print("eh equilatero")
    elif len(listaDeLados) == len(set(listaDeLados)):
        print("eh escaleno")
    elif len(listaDeLados)-1 == len(set(listaDeLados)):
        print("eh isosceles")

verificaTriangulo(lados)

    
