pgalao= float(input())
plitro= float(input())
cotacao= float(input())
galao= (pgalao/3.80) * cotacao
print("Gasolina EUA: R$ %.2f" %galao)
print("Gasolina Brasil: R$ %.2f" %plitro)
if(plitro>galao):
    print("Mais barata nos EUA")
elif(galao>plitro):
    print("Mais barata no Brasil")
else:
    print("Igual")