# coding=utf-8
a=int(input())
b=int(a/100)
c=int(a/10%10)
d=int(a%10)
if(b*b*b+c*c*c+d*d*d==a):
    print("YES")
else:
    print("NO")