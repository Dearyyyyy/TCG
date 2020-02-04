# coding=utf-8

from math import sqrt

n = int(input())
flag = 0
for i in range(2, int(sqrt(n))+1):
    if n % i == 0:
        flag = 1
if flag == 0:
    print("prime")
else:
    print("not prime")