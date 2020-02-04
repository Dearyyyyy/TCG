# coding=utf-8
n = int(input())
b=1
for i in range(n):
    s = input()
    a = len(s)
    for j in range(a):
        if s[j] != s[a - 1 - j]:
            b = 0
    if i!=n-1 :
        if b == 0:
            print("NO")
            b=1
        elif b == 1:
            print("YES")
            b=1
    elif i==n-1:
        if b == 0:
            print("NO",end="")
        elif b == 1:
            print("YES",end="")