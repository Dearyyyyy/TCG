# coding=utf-8
n = eval(input())
for i in range(n):
    string = input()
    if string == string[::-1]:
        print('YES')
    else:
        print('NO')