# coding=utf-8
N=int(input())
for i in range(N):
    a=input()
    result=a[::-1]
    if result==a:
        print('YES')
    else:
        print('NO')