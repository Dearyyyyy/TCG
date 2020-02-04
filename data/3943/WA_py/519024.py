# coding=utf-8
import itertools
while True:
    s = []
    p = []
    n = int(input())
    if n==0:
        break
    for i in range(1,n+1):
        s.append(i)
    p = list(itertools.permutations(s, n))
    for x in p:
        for y in x:
            print(y,end=" ")
        print("\b")