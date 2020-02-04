# coding=utf-8
n = int(input())
while True:
    m = int(input())
    if m>=100:
        b=m//100
    else:
        b=0
    m = m-100*b
    if m>=50:
        c=m//50
    else:
        c=0
    m = m-50*c
    if m>=20:
        d=m//20
    else:
        d=0
    m = m-20*d
    if m>=10:
        e=m//10
    else:
        e=0
    m = m-10*e
    if m>=5:
        f=m//5
    else:
        f=0
    m = m-5*f
    if m>=2:
        g=m//2
    else:
        g=0
    m = m-2*g
    if m==1:
        h=1
    else:
        h=0
    print(h,g,f,e,d,c,b)