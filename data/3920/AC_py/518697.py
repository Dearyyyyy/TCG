# coding=utf-8
n=input()
n=int(n)
a=n//100
b=(n-a*100)//10
c=n-a*100-b*10
d=a**3+b**3+c**3
if n==d:
   print("YES")
else:
   print("NO")