# coding=utf-8
while True:
    a,b=map(int,input().split())
    if b==0:
        print('error')
    else:
        c=a//b
        if (a-c*b)>=0.5*b:
            c=c+1
        print(c)