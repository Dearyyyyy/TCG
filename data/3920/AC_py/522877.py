# coding=utf-8
num = eval(input())
a = num%10
b = (num//10)%10
c = num//100
d = (pow(a,3) + pow(b,3) + pow(c,3))
if num == d:
    print("YES",end="")
else:
    print("NO",end="")