# coding=utf-8
n=int(input())

sum=0
a=2
b=1
for i in range(n):
    sum=sum+float(a/b)
    a,b=a+b,a

print("{:.2f}".format(sum))