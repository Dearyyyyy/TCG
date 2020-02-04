# coding=utf-8
n=int(input())
i=int((n/100))
j=int(n/10)%10
k=n%10
if n==i**3+j**3+k**3:
    print('YES')
else:
    print('NO')