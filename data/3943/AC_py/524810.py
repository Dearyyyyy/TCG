# coding=utf-8
import itertools
while True:
    try:
        N=int(input())
        if N==0:
            break
        else:
            array=[]
            for i in range(0,N,1):
                array.append(i+1)
            pailie = list(itertools.permutations(array))
            for x in pailie:
                for y in x:
                    print(y,end=' ')
                print() 
    except:
        break