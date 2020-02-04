# coding=utf-8
a=input()
a=int(a)
n=2
m=1
t=0
num=0
while(a):
    num=num+n/m
    t=m
    m=n
    n=n+t
    a=a-1
print('%.2f'%num)