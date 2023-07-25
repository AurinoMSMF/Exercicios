sal=float(input())
# a) salários até R$ 280.00 (incluindo) : aumento de 20%
# b)salários entre R$ 280.00 e R$ 700.00 : aumento de 15%
# c)salários entre R$ 700.00 e R$ 1500.00 : aumento de 10%
# d)salários de R$ 1500.00 em diante : aumento de 5% 
    # o salário antes do reajuste;
    # o percentual de aumento aplicado;
    # o valor do aumento;
    # o novo salário, após o aumento.
def trataSalario(sal):
    if sal>=0 and sal<=280.00:
        print("%.2f" %sal)
        print(20)
        aumento=sal*0.2
        print("%.2f" % aumento)
        novoSal=sal+aumento
        print("%.2f" % novoSal)
        
    elif sal>280.00 and sal<=700.00:
        print("%.2f" %sal)
        print(15)
        aumento=sal*0.15
        print("%.2f" % aumento)
        novoSal=sal+aumento
        print("%.2f" % novoSal)
        
    elif sal>700.00 and sal<1500.00:
        print("%.2f" %sal)
        print(10)
        aumento=sal*0.1
        print("%.2f" % aumento)
        novoSal=sal+aumento
        print("%.2f" % novoSal)
        
    elif sal>=1500:
        print("%.2f" %sal)
        print(5)
        aumento=sal*0.05
        print("%.2f" % aumento)
        novoSal=sal+aumento
        print("%.2f" % novoSal)

trataSalario(sal)