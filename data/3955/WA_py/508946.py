# coding=utf-8
n1,n2=input().split( )
n1=str(n1)
n2=str(n2)
if n2==n1[-1]+n1[:-1]:
    print('YES')
else:
    print('NO')