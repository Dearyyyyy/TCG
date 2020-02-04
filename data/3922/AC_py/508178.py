# coding=utf-8

while True:
    a,b=map(int,input().split())
    if b==0:
        print('error')
    elif a*2>=b and a%b!=0:
        print(a//b+1)
    else:
        print(a//b)