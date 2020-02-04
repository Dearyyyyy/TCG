# coding=utf-8
import math
s=input().split()
while s:
    a=int(s[0])
    b=int(s[1])
    if b==0:
        print("error")
    else:
        print(round(a/b))
    s = input().split()