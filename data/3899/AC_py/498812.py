# coding=utf-8
N = int(input())
a, b = 2, 1
s = 0
for i in range(N):
    s += a/b
    a, b = a+b, a
print("%.2f" % s)