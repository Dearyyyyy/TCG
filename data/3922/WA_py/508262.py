# coding=utf-8
while True:
    c = 0
    d = 0
    a,b=input().split(" ")
    if b==0:
        print("ERROR")
    else:
        c == a/b
        d = int(c)
        if (c-d)>=0.5:
            print(d+1)
        else:
            print(d)