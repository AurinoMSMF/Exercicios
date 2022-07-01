idadenadador= int(input())
if(5<=idadenadador and idadenadador<=7):
    print("Infantil A")
elif(8<=idadenadador and idadenadador<=10):
    print("Infantil B")
elif(11<=idadenadador and idadenadador<=13):
    print("Juvenil A")
elif(14<=idadenadador and idadenadador<=17):
    print("Juvenil B")
elif(18<=idadenadador and idadenadador<=40):
    print("Adulto")
elif(41<=idadenadador):
    print("Master")
else:
    print("Idade invalida.")
