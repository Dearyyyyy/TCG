# coding=utf-8
a=[100,50,20,10,5,2,1]
c=[]
n=int(input())
while n:
    x=int(input())
    for i in range(0,7):
        b=x/a[i]

        c.insert(0,int(b))
        d=int(b)
        x=x-a[i]*d
        while(x==0):
            break
    for i in range(0,6):
        print(c[i],end=' ')
    print(c[6])

    n-=1