# coding=utf-8
n = input()
q = 0
for i in n:
    q += int(i)**3
if q == int(n):
    print("YES")
else:
    print("NO")