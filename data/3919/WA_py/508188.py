# coding=utf-8
#-*-coding:utf-8-*-
while True:
    a,b,c=map(int,input().split())
    if a<b:
        temp=b
        b=a
        a=temp
    if a<c:
        temp=c
        c=a
        a=temp
    if b<c:
        temp=c
        c=b
        b=temp
    if a==b and b==c:
        print('DB')
    elif a==b or b==c or c==a:
        print('DY')
    elif b*b+c*c==a*a:
        print('ZJ')
    elif b+c>a:
        print('PT')
    else:
        print('ERROR')