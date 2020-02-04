# coding=utf-8
while True:
    a,b=input().split()
    if len(a)==len(b) and b in a+a:
        print("Yes")
    else:
        print("No")