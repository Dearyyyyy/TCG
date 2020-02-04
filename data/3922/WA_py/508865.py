# coding=utf-8
while True:
    a,b=input().split()
    if b==0:
        print("ERROR")
    a=int(a)
    b=int(b)
    c=a/b
    d=round(c)
    print(d)