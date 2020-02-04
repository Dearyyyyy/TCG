# coding=utf-8
N = int(input())
x2 = 1
for i in range(N-1):
    x1 = (x2+1)*2
    x2=x1
print(x1)