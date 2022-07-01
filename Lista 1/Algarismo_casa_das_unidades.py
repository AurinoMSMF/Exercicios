numero= int(input())
if(numero<0 and (numero!=0)):
    unidadenegativa=((numero*-1)%10)
    print("-{}" .format(unidadenegativa))
else:
    unidade= (numero% 10)
    print(unidade)