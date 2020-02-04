# coding=utf-8
import itertools
while True:
  N=int(input())
  if N==0:
      break
  array=[]
  i=1
  while i<=N:
        array.append(i)
        i+=1
  pailie = list(itertools.permutations(array))
  for x in pailie:
    for y in x:
        print(y,end=' ')
    print()