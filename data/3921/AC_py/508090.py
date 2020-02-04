# coding=utf-8
# this is a new learning program

n = eval(input())
for i in range(n):
    s = input()
    s2 = s[-1::-1]
    if s == s2:
        print('YES')
    else:
        print('NO')