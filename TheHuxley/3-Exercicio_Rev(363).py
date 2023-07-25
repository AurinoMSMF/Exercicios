def calcula(p,q,mod):
    if (mod=="*"):
        resultadoMulti=p*q
        return resultadoMulti
    elif(mod=="+"):
        resultadoSoma=p+q
        return resultadoSoma

n=int(input())

if((n>=1 and n<=500000) or (n<1 and n>=-500000)):
    
    p,mod,q=(input().split(" "))
    p=int(p)
    q=int(q)

    if(p>=0 and p<=1000) and (q>=0 and q<=1000):
        if(mod=="*"):
            resultado=calcula(p,q,mod)

        elif(mod=="+"):
            resultado=calcula(p,q,mod)

        if(resultado<=n):
            print("OK")

        else:
            print("OVERFLOW")
    else:
        print("OVERFLOW")
        
else:
        
    print("OVERFLOW")
        