# coding=utf-8
n=int(input())
a=n%10
b=n%100//10
c=n//100
if a*a*a+b*b*b+c*c*c==n:
    print('YES')
else:
    print('NO')