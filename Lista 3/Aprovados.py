portuguesnota = 0 
aprovados = [] 
while (portuguesnota>=0):
    portuguesnota = int(input())
    if (portuguesnota<0):
        break
    matematicanota = int(input())
    redacaonota = float(input())
    if (matematicanota>=21 and redacaonota>= 7 and portuguesnota>= 40):
        aprovados.append(1) 
print(len(aprovados))