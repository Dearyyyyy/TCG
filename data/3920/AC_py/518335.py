# coding=utf-8
n=int(input())
a=n//100
b=n%10
c=(n%100-b)/10
if n==a**3+b**3+c**3:
    print("YES")
else:
    print("NO")