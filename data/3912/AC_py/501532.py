# coding=utf-8
N=int(input())
flag=1
for i in range(2,N,1):
    if N%i==0:
        print("not prime")
        flag=0
        break
if flag==1:
    print("prime")