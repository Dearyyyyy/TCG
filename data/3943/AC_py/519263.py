# coding=utf-8
import itertools
while True:
    q = int(input())
    array = []
    for i in range(1,q+1):
        array.append(i)
    pailie = list(itertools.permutations(array))
    for x in pailie:
        for y in x:
            print(y,end=' ')
        print()