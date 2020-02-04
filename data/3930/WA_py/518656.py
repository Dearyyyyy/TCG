# coding=utf-8
while True:
    n = int(input())
    if n>=100:
        g = n//100
    else:
        g=0
    n = n-100*g
    if n>=50:
        f = n//50
    else:
        f=0
    n = n-50*f
    if n>=20:
        e = n//20
    else:
        e=0
    n = n-20*e
    if n>=10:
        d = n//10
    else:
        d==0
    n = n-10*d
    if n>=5:
         c = n//5
    else:
        c=0
    n = n-5*c
    if n>=2:
        b = n//2
    else:
        b = 0
    n = n-2*b
    a = n
    print(a,b,c,d,e,f,g)