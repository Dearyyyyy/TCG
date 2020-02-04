# coding=utf-8
n=int(input())
i=1
a=2
b=1
s=0
while i<=n:
    s=a/b+s
    t=a
    a=a+b
    b=t
    i+=1
print('%.2f'%s)