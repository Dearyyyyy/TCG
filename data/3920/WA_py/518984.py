# coding=utf-8
n=int(input())
a=n/100
b=n%100/10
c=n%100%10
if (a**3+b**3+c**3)==n:
    print('YES')
else:
    print('NO')