# coding=utf-8
a=int(input())
b=a//100
c=a%100//10
d=a%100%10
if(a==b**3+c**3+d**3):
    print("YES")
else:
    print("NO")