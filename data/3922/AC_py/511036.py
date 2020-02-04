# coding=utf-8
while(1):
    a,b = input().split()
    a=int(a)
    b=int(b)
    if b==0:
        print("error")
    else:
        c=a//b
        d=a%b
        if d*2>=b:
            print(c+1)
        else:
            print(c)