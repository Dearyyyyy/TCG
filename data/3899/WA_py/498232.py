# coding=utf-8
N=int(input())
sum=0

for t1 in range(1,N):
    for t2 in range(1,N):
        t1=n1
        t2=n2
        n1=t1+t2
        n2=t2
        s=n1/n2
        sum=sum+s
print(sum)