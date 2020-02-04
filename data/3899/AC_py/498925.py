# coding=utf-8
N=int(input())
a=2
b=1
sum=0
for i in range(N):
    sum=sum+a/b
    a,b=(a+b),a
print('{0:.2f}'.format(sum))