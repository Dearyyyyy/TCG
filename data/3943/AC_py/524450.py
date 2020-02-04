# coding=utf-8
import itertools
while True:
    n=int(input())
    if n==0:
        break
    else:
        a=[]
        for i in range(1,n+1):
            a.append(i)
        a=list(itertools.permutations(a))
        for j in a:
            for k in j:
                print(k,end=" ")
            print('')