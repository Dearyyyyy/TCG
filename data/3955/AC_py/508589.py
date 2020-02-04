# coding=utf-8
while True:
    try:
        c=0
        a,b=input().split()
        if len(a)!=len(b):
            print("No")
        else:
            a = a+a+a
            if b in a:
                print("Yes")
            else:
                print("No")
    except:
        break