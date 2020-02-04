# coding=utf-8
n = int(input())
b=1
for i in range(n):
    s = input()
    a = len(s)
    for j in range(a):
        if s[j] != s[a - 1 - j]:
            b = 0
    if b == 0:
        print("NO")
    elif b == 1:
        print("YES")