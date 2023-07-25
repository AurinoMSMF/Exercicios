n=int(input())
if(n>=1 and n<=40):
    stair=[]
    x=1
    while x<=n:
        stair.append(x)
        print(*stair)
        x+=1