# coding=utf-8
import itertools
while True:
    m = int(input())
    array = []
    for i in range(1,m+1):
        array.append(i)
    pailie = list(itertools.permutations(array))
    for x in pailie:
        for y in x:
            print(y,end=' ')
        print()