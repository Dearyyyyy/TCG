# coding=utf-8
import itertools
while 1:
    n=int(input())
    array=[]
    for i in range(1,n+1):
        array.append(i)
    pailie = list(itertools.permutations(array))
    for x in pailie:
        for y in x:
            print(y,end=' ')
        print()
    if n==0:
        break