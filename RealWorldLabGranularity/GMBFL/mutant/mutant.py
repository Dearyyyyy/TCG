# coding=utf-8
while True:
    a,b=map(int,input().split(" "))
    if b==0:
        print("error")
    else:
        c=a//b
        d=int(c)
        if (c-d)>=1//2:
            e=d+1
        else:
            e=d
        print(e)
