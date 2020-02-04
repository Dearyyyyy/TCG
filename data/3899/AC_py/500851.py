# coding=utf-8
a=1
b=2
l=[]
l.append(b/a)
n=int(input())
for i in range(n-1):
    c=a
    a=b
    b=b+c
    l.append(b/a)
sum0=sum(l)
print("%.2f"%sum0)