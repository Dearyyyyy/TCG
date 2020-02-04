# coding=utf-8
import itertools
while True:
    n = int(input())
    array = []
    for i in range(1,n+1):
        array.append(i)
    A = list(itertools.permutations(array))
    for x in A:
        for y in x:
            print(y,end="")
        print()