# coding=utf-8
N=int(input())
for i in range(2,N):
    if N%i==0:
        print("not prime")
        break;
          
    if N%i!=0:
        print("prime")
        break;