# coding=utf-8
while True:
    a,b=input().split(" ")
    if b==0:
        print("error")
    else:
        c = a/b
        d = int(c)
        if (c-d)>=0.5:
            e=d+1
        else:
            e=d
        print(e)