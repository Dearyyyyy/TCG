# coding=utf-8
while True:
    a,b=input().split()
    a1=a+a
    if a1.find(b)!=-1:
        print("Yes")
    else:
        print("No")