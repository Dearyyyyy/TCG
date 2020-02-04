# coding=utf-8
import itertools
while True:
    n=int(input())
    if(n==0):
        break
    else:
        pailie = list(itertools.permutations(range(1,n+1)))
        for x in pailie:
            for y in x:
                print(y,end=' ')
            print()