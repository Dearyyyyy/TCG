# coding=utf-8
from itertools import *
if __name__ == '__main__':
    while True: 
        m = []
        i = 1
        a = int(input())
        if a==0:
            break
        else:
            while i <= a:
                m.append(i)
                i=i+1
        for i in permutations(m):
            print(i)