# coding=utf-8

import itertools
while True:
    s=int(input())
    if(s==0):
        break
    else:
        pailie = list(itertools.permutations(range(1,s+1)))
        for t in pailie:
            for y in t:
                print(y,end=' ')
            print()