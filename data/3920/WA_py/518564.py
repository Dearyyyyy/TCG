# coding=utf-8
n = int(input())
a = n%10
b = n%100/10
c = n//10
num = a**3+b**3+c**3
if num == n:
    print("Yes")
else:
    print("No")