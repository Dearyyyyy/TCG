# coding=utf-8
n=int(input())
for i in range(n):
    a=b=c=d=e=f=g=0
    x=int(input())
    if(x>=100):
        x1=x//100
        g=x1
        x=x-(x1*100)
    if(x>=50):
        x1=x//50
        f=x1
        x=x-(x1*50)
    if(x>=20):
        x1=x//20
        e=x1
        x=x-(x1*20)
    if(x>=10):
        x1=x//10
        d=x1
        x=x-(x1*10)
    if(x>=5):
        x1=x//5
        c=x1
        x=x-(x1*5)
    if(x>=2):
        x1=x//2
        b=x1
        x=x-(x1*2)
    a=x
    print(a,b,c,d,e,f,g)