# coding=utf-8
n=int(input())
a=2
b=1 
sum=0 
for i in range(n):
    sum=sum+a/b 
    a=a+b 
    b=a-b 
print("%.2f"%sum)