# coding=utf-8
while True:
    a,b=input().split()
    a=float(a)
    b=float(b)
    if b==0:
        print("error")
    else:
        c=a/b+0.5
        c=int(c)
        print(c)