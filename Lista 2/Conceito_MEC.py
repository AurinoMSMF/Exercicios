livros=int(input())
alunos=int(input())
conceito= alunos/livros
if(conceito<=8):
    print("A")
elif(9<=conceito and conceito<=12):
    print("B")
elif(13<=conceito and conceito<=18):
    print("C")
elif(conceito>18):
    print("D")