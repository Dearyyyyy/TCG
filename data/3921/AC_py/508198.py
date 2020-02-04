# coding=utf-8
a=int(input())
i=0
while i<a:
    i=i+1
    str=input()
    if str==str[::-1]:
        print('YES')
    else:
        print('NO')