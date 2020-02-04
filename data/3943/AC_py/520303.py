# coding=utf-8
import itertools
while 1:
    x = []
    n = int(input())
    for i in range(1,n+1):
        x.append(i)
    qp = list(itertools.permutations(x))
    for i in qp:
        for j in i:
            print(j,end = ' ')
        print()