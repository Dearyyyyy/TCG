# coding=utf-8
a=int(input())
b=int(a/100%10)
c=int(a/10%10)
d=int(a/1%10)
if b**3+c**3+d**3==a:
    print("YES")
else:
    print("NO")