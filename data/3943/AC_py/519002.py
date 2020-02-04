# coding=utf-8
from itertools import *
if __name__ == '__main__':
    while True: 
        m = []
        i = 1
        n = 0
        a = int(input())
        if a==0:
            break
        else:
            while i <= a:
                m.append(i)
                i=i+1
        for i in permutations(m):
            for ele in i:
                print(ele,end=' ')
                n = n+1
                if n%a==0:
                    print()