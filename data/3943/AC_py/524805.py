# coding=utf-8
import itertools
while True:
    a=int(input())
    b=[]
    for i in range(1,a+1):
        b.append(i)
    l=list(itertools.permutations(b,a))
    for i in l:
        print(*i)