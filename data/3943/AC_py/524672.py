# coding=utf-8
import itertools
while True:
    n=int(input())
    s=[]
    for i in range(1,n+1):
        s.append(i)
    list2=list(itertools.permutations(s,n))
    for i in list2:
        print(*i)