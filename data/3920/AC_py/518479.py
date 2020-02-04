# coding=utf-8
n = int(input())
a = n%10
b = n//100
c = (n-b*100-a)//10
if n == a ** 3 + b ** 3 + c ** 3:
        print('YES')
else:
        print('NO')