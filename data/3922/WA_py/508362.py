# coding=utf-8
value = 0
while True :
    a,b=input().split()
    a=int(a)
    b=int(b)
    if b==0 :
        print("error")
    else :
        value=a//b
        print(value)