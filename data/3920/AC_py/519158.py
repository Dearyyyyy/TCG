# coding=utf-8
a=int(input())
b=a%10
c=a//100
d=a//10%10
if c*c*c+d*d*d+b*b*b==a:
    print("YES")
else:
    print("NO")