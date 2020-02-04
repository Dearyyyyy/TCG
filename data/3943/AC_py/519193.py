# coding=utf-8
from itertools import permutations
arr = []
while True:
    n = int(input())
    if n==0:
        break
    else:
        for i in range(n):
            arr.append(i+1)
        for x in permutations(arr):
            for j in range(len(x)):
                print(x[j],end=' ')
            print()
            arr = []