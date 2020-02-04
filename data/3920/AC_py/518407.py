# coding=utf-8
a=int(input())
b=a//100
c=(a%100)//10
d=a%10
if (b*b*b+c*c*c+d*d*d)==a:
    print("YES")
else :
    print("NO")