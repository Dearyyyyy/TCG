# coding=utf-8
s=[100,50,20,10,5,2,1]
t=[]
n=int(input())
while n:
    x=int(input())
    for i in range(0,7):
        b=x/s[i]

        t.insert(0,int(b))
        d=int(b)
        x=x-s[i]*d
        while(x==0):
            break
    for i in range(0,6):
        print(t[i],end=' ')
    print(t[6])

n-=1