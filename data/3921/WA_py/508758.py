# coding=utf-8
while True:
    s = input()
    a = reversed(list(s))
    if list(a) == list(s):
        print('YES')
    else:
        print('NO')