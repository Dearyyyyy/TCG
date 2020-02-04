# coding=utf-8
while True:
    a,b = map(str,input().split())
    c = a
    if len(a)==len(b):
        a = "a"+"c"
        if a.find(b) ==1:
            print("Yes")
        else:
            print("No")
    else:
        print("No")