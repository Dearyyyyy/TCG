# coding=utf-8
n = eval(input())
a = 0
b = 1
i = 1
while i<n:
   i += 1
   a = (b + 1) * 2
   b = a
print(a)