# coding=utf-8
a=int(input())
b=a%100//10
c=a%10
d=a//100
if d**3+b**3+c**3==a:
    print("YES")
else :
    print("NO")