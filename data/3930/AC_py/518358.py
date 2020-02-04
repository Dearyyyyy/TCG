# coding=utf-8
b=int(input())
for k in range(b):
    a=int(input())
    b=[0,0,0,0,0,0,0]
    while(a>0):
        if(a>=100):
            b[6]+=1
            a=a-100
        elif(a>=50):
            b[5]+=1
            a=a-50
        elif(a>=20):
            b[4]+=1
            a=a-20
        elif(a>=10):
            b[3]+=1
            a=a-10
        elif(a>=5):
            b[2]+=1
            a=a-5
        elif(a>=2):
            b[1]+=1
            a=a-2
        elif(a>=1):
            b[0]+=1
            a=a-1
    for i in b:

        print(i,end=" ")
    print()