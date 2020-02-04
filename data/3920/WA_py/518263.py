# coding=utf-8
a=int(input())
b=a/100
c=a/10%10
d=a%10
if(b**3+c**3+d**3==a):
    print("YES")
else:
    print("NO")