# coding=utf-8
a=int(input())
for i in range(a):
    b=input()
    c=b[::-1]
    if b==c:
        print('YES')
    else:
        print('NO')