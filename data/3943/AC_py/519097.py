# coding=utf-8
import itertools
while True:
    n=int(input())
    a=[i for i in range(1,n+1)]
    res = list(itertools.permutations(a))
    for x in res:
        for y in x:
            print(y,end=' ')
        print()
    if n==0:
        break