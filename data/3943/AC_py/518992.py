# coding=utf-8
import itertools
while True:
        n=input()
        n=int(n)
        s1 = []
        if n==0 :
            break
        else:
            for i in range (1,n+1) :
                s1.append(i)
            pailie = list(itertools.permutations(s1))
            for x in pailie:
                for y in x:
                    print(y,end=' ')
                print()