# coding=utf-8
b=1
a=1
s=0
N=int(input())
for i in range(1,N+1):
    c=b
    b=a
    a=a+c
    s=s+a/b
print('%.2f'%s)