Cv , Ce, Cs, Fv, Fe, Fs = input().split(" ")
Cv=int(Cv)
Ce=int(Ce)
Cs=int(Cs)
Fv=int(Fv)
Fe=int(Fe)
Fs=int(Fs)
Cv = Cv*3
Fv = Fv*3
vit_emp1= Cv + Ce
vit_emp2= Fv + Fe

if(vit_emp1>vit_emp2):
    print("C")
elif(vit_emp2>vit_emp1):
    print("F")
elif(vit_emp1 == vit_emp2):
    if (Cs>Fs):
        print("C")
    elif(Fs>Cs):
        print("F")
    else:
        print("=")