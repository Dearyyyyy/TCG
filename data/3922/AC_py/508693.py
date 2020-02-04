# coding=utf-8
while True:
    a,b=input().split()
    a=int(a)
    b=int(b)
    if b==0:
        print("error")
    else :
        c=a/b
        if c-int(c)>=0.5:
            print(int(c)+1)
        else :
            print(int(c))