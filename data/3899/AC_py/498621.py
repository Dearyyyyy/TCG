# coding=utf-8
n=int(input())
s=0
a=2
b=1
for i in range(1,n+1):
    s+=a/b
    t=a
    a=a+b
    b=t
print('%.2f'%s)