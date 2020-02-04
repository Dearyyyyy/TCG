# coding=utf-8
N=int(input())
a=2
b=1
sum=0
for i in range(N):
   sum=sum+a/b
   a=a+b
   b=a-b
print("%.2f"%sum)