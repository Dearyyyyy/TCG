# coding=utf-8
n=input()
n=int(n)
a=n%10
b=int(n/10)%10
c=int(n/100)
if n==a**3+b**3+c**3:
    print('YES')
else:
    print('NO')