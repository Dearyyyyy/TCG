# coding=utf-8
while(1):
    a=[]
    b=[]
    A=[]
    e=0
    a,b=input().split()
    for i in range(len(a)):
        A.append(a[i])
    for i in range(len(b)-1):
        c=[]
        for j in range((len(b)-1)):
            x=b[0]
            c.append(b[j+1])
        c.append(x)
        b=c
        if(A==c):
            print("Yes")
            e=1
            break
    if(e==0):
        print("No")