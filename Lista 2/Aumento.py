salario=float(input())
if(salario<=280):
    aumento1=salario+(salario*0.20)
    print(aumento1)
elif(280<salario<=700):
    aumento2=salario+(salario*0.15)
    print(aumento2)
elif(700<salario<=1500):
    aumento3=salario+(salario*0.10)
    print(aumento3)
elif(salario>1500):
    aumento4=salario+(salario*0.05)
    print(aumento4)



