# coding=utf-8
a,b=2,1
sum=0
n=int(input())
i=1
for i in range (0,n):
    sum=(a/b)+sum
    a=a+b
    b=a-b
    i=i+1
print(round(sum,2))