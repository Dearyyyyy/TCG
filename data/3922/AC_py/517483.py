# coding=utf-8
while True:
    a,b=input().split()
    a=int(a);b=int(b)
    if b==0:print('error')
    else:print(int(a*1.0/b+0.5))