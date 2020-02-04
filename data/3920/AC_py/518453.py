# coding=utf-8
a=int(input())
x=a//100
y=a//10%10
z=a%10
if x*x*x+y*y*y+z*z*z==a:
    print('YES')
else:
    print('NO')