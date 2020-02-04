# coding=utf-8
n=int(input())
for i in range(n):
    s=input()
    t=s[::-1]
    if s==t:
        print('YES')
    else:
        print('NO')