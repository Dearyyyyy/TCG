# coding=utf-8
while True:
    a,b=input().split()
    a=float(a)
    b=float(b)
    s=a/b
    i=s%1
    c=int(s)
    if i>=0.5:
        c=c+1
    else:
        c=c
    print(c)