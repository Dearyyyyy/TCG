# coding=utf-8
n = int(input())
a = 2
b = 1
i = 0
sum = 0
while i < n:
    sum = sum+a/b
    a,b = a+b,a
    i = i+1
print("%.2f" % sum)