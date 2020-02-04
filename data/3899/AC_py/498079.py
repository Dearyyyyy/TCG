# coding=utf-8
a=float(input())
i=0
b=1
c=2
sum1=0
while(i<a):
    sum1=sum1+c/b
    k=c
    c=c+b
    b=k
    i=i+1
print("%.2f"%sum1)