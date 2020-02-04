# coding=utf-8
a=int(input())
b=a//100
c=a%100//10
d=a%10
if a==b*b*b+c*c*c+d*d*d:
    print("YES")
else:
    print("NO")