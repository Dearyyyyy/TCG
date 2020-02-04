# coding=utf-8
from itertools import permutations
while True:
    n = int(input())
    array = []
    for i in range(1,n+1):
        array.append(i)
    pailie = list(permutations(array))#要list一下，不然它只是一个对象
    for x in pailie:
        for y in x:
            print(y,end=' ')
        print()