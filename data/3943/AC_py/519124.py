# coding=utf-8
import itertools
while True:
    a=int(input())
    s=[]
    for i in range(1,a+1):
        s.append(i)
    pailie=list(itertools.permutations(s))
    for x in pailie:
        for y in x:
            print(y,end=' ')
        print()