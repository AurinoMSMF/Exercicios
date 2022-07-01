kwh=float(input())
valortotal=float
valortotal=float(kwh*1.5)
valordesc=float
valordesc=float(valortotal-(valortotal*(15/100)))
print("Valor a ser pago: R$ %.2f reais" %(valortotal))
print("Valor a ser pago com desconto: R$ %.2f reais" %(valordesc))