# coding=utf-8
N=int(input())
a=2
b=1
sum=0
for i in range(0,N):
    sum=sum+a/b
    c=a
    a=a+b
    b=c
print("%.2f" % sum)