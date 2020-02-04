# coding=utf-8
a=int(input())
a1=a//100
a2=a//10%10
a3=a%10
if a1**3+a2**3+a3**3==a:
    print('YES')
else:
    print('NO')