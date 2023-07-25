n=int(input())
periodicidade=int(input())
x=0
doses=3
anosDeVacina=[]
for i in range(doses):
    n+=periodicidade
    anosDeVacina.append(n)
    x+=1
print(*anosDeVacina, end="")