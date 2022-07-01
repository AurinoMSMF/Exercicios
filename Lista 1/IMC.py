massa= float(input())
altura= float(input())
if(1<=massa<=500 and 1<=altura<2.8):
    imc = (massa/(altura**2))
    print("%.2f" %(imc))
else:
    print()
    