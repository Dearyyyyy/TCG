# coding=utf-8
import itertools
while True:
    n = int(input())
    array = []
    for i in range(1,n+1):
        array.append(i)
    pailie = list(itertools.permutations(array))#要list一下，不然它只是一个对象
    for x in pailie:
        for y in x:
            print(y,end=' ')
        print()