# coding=utf-8
while True:
    a,b = map(str,input().split())
    if len(a)==len(b):
        a = a+a
        if a.find(b) ==1:
            print("Yes")
        else:
            print("No")
    else:
        print("No")