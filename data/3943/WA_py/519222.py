# coding=utf-8
import itertools
while True:
    n=int(input())
    numlist=[]
    i=0
    for i in range(0,n):
        numlist.append(i+1)
        i=i+1
    for i in itertools.permutations(numlist[0:n], n):
        print (i)