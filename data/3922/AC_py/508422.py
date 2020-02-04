# coding=utf-8
while True:
    try:
        a,b=input().split()
        a=int(a)
        b=int(b)
        if b!=0:
            c=a/b
            d=a//b
            if c-d>=0.5:
                d=d+1
            print(d)
        else:
            print("error")
    except:
        break