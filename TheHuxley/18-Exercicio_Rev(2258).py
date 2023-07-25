def retornaNumeroCaracteres(s):
    s=list(s)
    x=0
    for i in s:
        if i:
            x+=1
    return x
s=input()
if len(s)<=50:
    print(retornaNumeroCaracteres(s))
else:
    pass