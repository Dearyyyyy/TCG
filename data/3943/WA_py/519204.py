# coding=utf-8
import itertools
while True:
    m = int(input())
    a = []
    for i in range(1,m+1):
        a.append(i)
    pailie = list(itertools.permutations(a))
    for j in pailie:
        for k in j:
            print(k,end='')
        print()