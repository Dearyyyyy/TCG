# coding=utf-8
n = int(input())
a = int(n/100)
b = int(n/10%10)
c = int(n%10)
if n == a*a*a+b*b*b+c*c*c:print('YES')
else:print('NO')