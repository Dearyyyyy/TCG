# coding=utf-8
a=int(input())
i=2
flag=1
while(i<a):
    if a%i==0:
        flag=0
    i+=1
if flag==1:
    print("prime")
else:
    print("not prime")