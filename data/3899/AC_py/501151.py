# coding=utf-8
n=int(input())
a=1
b=2
sum=0
for i in range(1,n+1):
    sum+=b/a
    c=a+b
    a,b=b,c
print("%.2f"%sum)