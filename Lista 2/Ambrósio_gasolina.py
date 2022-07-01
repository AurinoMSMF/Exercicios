D, R, L, P, G=input().split()
D=int(D)
R=int(R)
L=int(L)
P=int(P)
G=int(G)
A=L*10
A=int(A)
SOBRA=R - ((D/10)-L)*G
SOBRA=int(SOBRA)
if(D>=0 and R>=0 and L>=0 and P>=0 and G>=0 and A>=D/(P+1) and SOBRA>=0):
    print("Pode viajar.")
    print("R$:", SOBRA)
else:
    print("Nao pode viajar.")


