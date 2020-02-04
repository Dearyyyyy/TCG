# coding=utf-8
a=int(input())
b=1
for i in range(2,a):
    if a%i==0:
       b=0
if b!=0:
    print("prime")