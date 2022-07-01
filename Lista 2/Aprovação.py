n1=float(input("Informe a primeira nota:"))
print()
n2=float(input("Informe a segunda nota:"))
print()
n3=float(input("Informe a terceira nota:"))
print()
media=(n1+n2+n3)/3
if(media >= 7.0):
    print("Aprovado com media %.1f" %media)
elif(5.0<=media<7.0):
    print("Recuperacao com media %.1f" %media)
elif(media<5.0):
    print("Reprovado com media %.1f" %media)

