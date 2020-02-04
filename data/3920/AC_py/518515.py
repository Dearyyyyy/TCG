# coding=utf-8
N=int(input())
a=N//100
c=N%10
b=(N//10)%10
if N==a**3+b**3+c**3:
       print("YES")
else:
    print("NO")