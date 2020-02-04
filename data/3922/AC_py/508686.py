# coding=utf-8
while True:
    a,b=input().split()
    a=int(a)
    b=int(b)
    if b!=0:
        c=a/b
        if c%1>=0.5:
            c=a//b+1
        else:
            c=a//b
        print(c)
    else:
        print('error')