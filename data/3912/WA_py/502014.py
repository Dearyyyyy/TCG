# coding=utf-8
from math import *
n = input()
n = int(n)
i=2
while i <= sqrt(n):
    if n%i ==0:
        break
    else:
        n +=1
if(i<int(sqrt(n))):
    print('prime')
else:
    print('not prime')