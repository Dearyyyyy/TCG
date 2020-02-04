# coding=utf-8
import itertools
while True:
    n=int(input())
    if n==0:
        break
    a=[]
    for i in range(1,n+1):
        a.append(i)
    b=itertools.permutations(a,n)
    for m in b:
        for s in m:
            print(s,end=' ')
        print()