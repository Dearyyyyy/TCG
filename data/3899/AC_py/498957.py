# coding=utf-8
N=int(input())
s=0
a=1
b=1
for i in range(1,N+1):
    c=b
    b=a+b
    a=c
    n=b/a
    s=s+n
print("%.2f"%s)