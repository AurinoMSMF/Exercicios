def retornaRaizes(a,b,c):
    delta=(b**2)-4*(a)*(c)
    raizes=0
    if delta<0:
        print(raizes)
    else:
        x1=-(b+(delta**0.5))/2*a
        x2=-(b-(delta**0.5))/2*a

        raiz1=a*(x1**2)+b*x1+c
        raiz2=a*(x2**2)+b*x2+c

        if(raiz1==0 and raiz2==0):
            if(x1==x2):
                if(x1==-0):
                    x1=x1*-1
                    print("%.2f"%x1)
                else:
                    print("%.2f"%x1)
                raizes=1
            else:
                print("%.2f %.2f"%(x2,x1))
                raizes=2
        elif(raiz1==0 and raiz2!=0):
            if(x1==-0):
                x1=x1*-1
                print("%.2f" %x1)
            else:
                print("%.2f" %x1) 
            raizes=1
        elif(raiz1!=0 and raiz2==0):
            if(x2==-0):
                x2=x2*-1
                print("%.2f" %x2)
            else:
                print("%.2f" %x2)                
            raizes=1
        elif(raiz1!=0 and raiz2!=0):
            raizes=0

    print(raizes)

a,b,c=input().split(" ")

a=int(a)
b=int(b)
c=int(c)

retornaRaizes(a,b,c)