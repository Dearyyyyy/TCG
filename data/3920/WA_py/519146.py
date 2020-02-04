# coding=utf-8
a=int(input())
b=a%10
c=a/100
d=a/10%10
if c**3+d**3+b**3==a:
    print("YES")
else:
    print("NO")