# coding=utf-8
a=int(input())
k=0
for i  in range(1,a+1):
    if a%i==0:
        k=k+1
if k==2:
    print("prime")
else:
    print("not prime")