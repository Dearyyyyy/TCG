# coding=utf-8
n = int(input())
for i in range(n):
    s = input()
    a = reversed(list(s))
    if list(a) == list(s):
        print("YES")
    else:
        print("NO")