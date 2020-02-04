# coding=utf-8
N = int(input())
a = 1
b = 2
c = 0
S_sum = 0
for ii in range(1,N+1):
    c = a + b
    S_sum += b/a
    a = b
    b = c
print("%.2f" % S_sum)