# coding=utf-8
n = int(input())

while n > 0:
    n -= 1
    s = input()
    result = True
    l = len(s)
    for i in range(l):
        if s[i] != s[l-i-1]:
            result = False
            break
    if result:
        print('YES')
    else:
        print("NO")