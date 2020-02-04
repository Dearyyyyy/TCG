# coding=utf-8
import itertools
while True:
    n = eval(input())
    l = []
    i = 1
    while i<=n:
        l.append(i)
        i += 1
    tar = list(itertools.permutations(l,n))
    for item in tar:
        for s in item:
            print(s,end = " ")
        print()