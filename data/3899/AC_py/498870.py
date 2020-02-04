# coding=utf-8
N= int(input())
a=1
b=2
s=2
s=float(s)
for i in range(N-1):
   a,b=b,a+b
   s=s+float(b/a)
print("%.2f"%s)