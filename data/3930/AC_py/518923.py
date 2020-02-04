# coding=utf-8
a=int(input())
for i in range(a):
    n=int(input())
    if n>=100:
        a=n//100
    else:
        a=0
    n=n-100*a
    if n>=50:
        b=n//50
    else:
        b=0
    n=n-50*b
    if n>=20:
        c=n//20
    else:
        c=0
    n=n-20*c
    if n>=10:
        d=n//10
    else:
        d=0
    n=n-10*d
    if n>=5:
        e=n//5
    else:
        e=0
    n=n-5*e
    if n>=2:
        f=n//2
    else:
        f=0
    n=n-2*f
    g=n
    print(g,f,e,d,c,b,a)