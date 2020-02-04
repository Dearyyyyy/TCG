# coding=utf-8
while True:
    a,b=map(int,input().split())
    if b==0:
        print('error')
        
    elif a<b:
        if a>=b/2:
            print(1)
        else:
            print(0)
    elif a>=b:
        if a%b>=b/2:
            print(a//b+1)
        else:
            print(a//b)