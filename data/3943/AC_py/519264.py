# coding=utf-8
import itertools
while True:
    n=int(input())
    if n==0:
        break
    numlist=[]
    i=0
    for i in range(0,n):
        numlist.append(i+1)
        i=i+1
    for i in itertools.permutations(numlist[0:n], n):
        k=0
        for j in i:
            print(j,end=' ')
            k=k+1
            if k==n:
                print()