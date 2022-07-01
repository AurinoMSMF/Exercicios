media, numaulas, faltas= input().split()
media=float(media)
numaulas=float(numaulas)
faltas=float(faltas)
presen�a= numaulas-faltas
presen�a=float(presen�a)
frequencia= ((100/(numaulas/presen�a))/100)
frequencia=float(frequencia)
if(media>=5 and frequencia>=0.75):
    print("APROVADO")
elif(media>=7 and frequencia>=0.50):  
    print("APROVADO")
else:
    print("REPROVADO")
