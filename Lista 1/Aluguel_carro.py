dias= int(input())
kmrodados= int(input())
vdias= dias*30
vkmrodados= kmrodados*0.01
valortotal= vdias+vkmrodados
valortotaldesc=valortotal-(valortotal*0.10)
if(1<=dias<=30 and 1<=kmrodados<=1000):
    print("%.2f" %(valortotaldesc))
else:
    print()