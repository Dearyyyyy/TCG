# coding=utf-8
while True:
    try:
        a,b=input().split()
        a=int(a)
        b=int(b)
        if b==0:
            print("error")
        else:
            e=(a+(b/2))/b
            print("%d"%e)
    except:
        break