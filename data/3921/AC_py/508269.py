# coding=utf-8
n=int(input())
i=0
while i<n:
    str1=input()
    if str1[::-1]==str1:
        print('YES')
    else:
        print('NO')
    i=i+1