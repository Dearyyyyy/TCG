# coding=utf-8
N=int(input())
a=2
b=1
s=0
for i in range(1,N+1):
    s+=a/b
    a,b=(a+b),a
print('%.2f'%s)