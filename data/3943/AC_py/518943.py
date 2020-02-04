# coding=utf-8
import itertools
while True:
    n=int(input())
    s=[]
    for i in range(1,n+1):
        s.append(i)
    l=list(itertools.permutations(s,n))
    for i in l:
        print(*i)