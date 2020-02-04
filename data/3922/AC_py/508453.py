# coding=utf-8
import math
s=input().split()
while s:
    a=int(s[0])
    b=int(s[1])
    if b==0:
        print("error")
    else:
        c=int(a/b)
        if (a/b-c)<0.5:
            print(c)
        else:
            print(c+1)
    s = input().split()