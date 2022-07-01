nimas=int(input())
imas=[]
imas.append(input())
group=1
codigigual=1
biggest=1
for iman in range(1, nimas):
    imas.append(input())
    if (imas[iman-1] == imas[iman]):
        codigigual= codigigual +1
        if (codigigual > biggest):
            biggest= biggest +1
    else:
        group= group +1
        codigigual= 1

print("groups: {}, biggest: {}".format(group, biggest))