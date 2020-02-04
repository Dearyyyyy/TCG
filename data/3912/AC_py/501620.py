# coding=utf-8
n=eval(input())
f=0
for i in range(2,n):
    if n%i==0:
        f=1
if f==1:
    print("not prime")
else :
    print("prime")