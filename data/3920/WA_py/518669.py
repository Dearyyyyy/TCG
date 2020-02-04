# coding=utf-8
a,b,c = input()
a = int(a)
b = int(b)
c = int(c)
num = 100*a+10*b+c
if num == a*a*a+b*b*b+c*c*c:
   print("YES") 
else:
   print("NO")