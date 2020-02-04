# coding=utf-8
a=int(input())
i=2
while i<a:
    if a%i==0:
        print("not prime")
        break
    i=i+1
if i==a:
    print("prime")