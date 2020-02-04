# coding=utf-8
n=int(input())
flag=0
i=2
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
    else:
        flag=1
if flag==1:
    print("prime")