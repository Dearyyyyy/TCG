# coding=utf-8
while True:
    try:
        c=0
        a,b=input().split()
        a = a + a+a
        if b in a:
            print("Yes")
        else:
            print("No")
    except:
        break