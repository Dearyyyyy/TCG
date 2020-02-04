# coding=utf-8

from math import*
n=int(input())

a=2
b=1
sum=2.00
for i in range(n-1):
    n=a
    a=a+b
    b=n
    sum+=a/b
print("%.2f"%sum)