# coding=utf-8
n=int(input())
for i in range(3):
    a=n//100
    b=n%100//10
    c=n%10
    s=a**3+b**3+c**3
if s==n:
    print('YES')
else:
    print('NO')