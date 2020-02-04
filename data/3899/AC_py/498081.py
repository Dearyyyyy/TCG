# coding=utf-8
N = int(input())
a = 1
b = 2
sum = 0
for i in range(N):
    sum+=b/a
    a,b = b,a+b
print("%.2f"%sum)