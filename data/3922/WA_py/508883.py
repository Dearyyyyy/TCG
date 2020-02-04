# coding=utf-8
while True:
    a,b=input().split()
    a=int(a)
    b=int(b)
    if b==0:
        print("ERROR")
    else:
        c=a/b
        d=int(c+0.5)
        print(d)