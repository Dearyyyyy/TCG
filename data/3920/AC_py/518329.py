# coding=utf-8
n = input()
s = 0
for i in n:
    s += int(i)**3
if s == int(n):
    print("YES")
else:
    print("NO")