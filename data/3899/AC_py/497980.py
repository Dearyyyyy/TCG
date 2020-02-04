# coding=utf-8
a=2
b=1
s=0
n=int(input())
for i in range(1,n+1):
    c=a/b
    s=s+c
    k=a
    a=a+b
    b=k
    
    
print("%.2f"%s)