# coding=utf-8
n=int(input())
k=[]
for j in range (7):
    k.append(0)
for i in range (n):
    a=int(input())
    for p in range (7):
        k[p]=0
    while True:
        if a>=100:
            a=a-100
            k[6]+=1
        else:
            break
    while True:
        if a>=50:
            a=a-50
            k[5]+=1
        else:
            break
    while True:
        if a>=20:
            a=a-20
            k[4]+=1
        else:
            break
    while True:
        if a>=10:
            a=a-10
            k[3]+=1
        else:
            break
    while True:
        if a>=5:
            a=a-5
            k[2]+=1
        else:
            break
    while True:
        if a>=2:
            a=a-2
            k[1]+=1
        else:
            break
    while True:
        if a>=1:
            a=a-1
            k[0]+=1
        else:
            break
    for u in range(len(k)):
        print(k[u],end=' ')
    print("")