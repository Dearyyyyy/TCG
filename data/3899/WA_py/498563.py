# coding=utf-8
N=int(input())
a1=2
a2=3
b1=1
b2=2
sum1=a1/b1+a2/b2
for i in range(3,N+1):
    a1=a1+a2
    a2=a1
    b1=b1+b2
    b2=b1
    sum1=sum1+a1/b1
print('{0:.2f}'.format(sum1))