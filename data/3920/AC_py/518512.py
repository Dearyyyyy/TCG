# coding=utf-8
n=int(input())
a=n//100
b=n%100//10
c=n%100%10
if n==a*a*a+b*b*b+c*c*c:
    print('YES')
else:
    print('NO')