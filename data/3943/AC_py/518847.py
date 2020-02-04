# coding=utf-8
from itertools import permutations
while True:
    n=eval(input())
    list=[]
    for i in range (1,n+1):
        list.append(i)
    for j in permutations(list):
        for i in j:
            if i>=0 and i<=9:
                print(i,end=' ')
        print()