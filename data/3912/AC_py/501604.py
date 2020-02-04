# coding=utf-8
N=int(input())
i=2
a=0
for i in range(2,N):
    if  N%i==0:
         print("not prime")
         break
    else:
        a=a+1
        
if a!=0:
    print("prime")