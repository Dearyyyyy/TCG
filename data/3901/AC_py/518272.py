# coding=utf-8
def s(N):
    a=1
    for i in range(1,N):
     a=(a+1)*2
    return a
N=int(input())
k=s(N)
print(k)