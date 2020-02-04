# coding=utf-8
import string
while  True:
    n=input()
    a=a.count('1Y')
    b=a.count('1N')
    c=a.count('2Y')
    d=a.count('2N')
    e=a.count('3Y')
    f=a.count('3N')
    g=a.count('R')
    h=a.count('A')
    j=a.count('S')
    k=a.count('B')
    l=a.count('T')
    s=a+c*2+e*3+g+h+j+k-d-f-b-l
    print(s)