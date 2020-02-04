# coding=utf-8
import string
while  True:
    n=input()
    a=n.count('1Y')
    b=n.count('1N')
    c=n.count('2Y')
    d=n.count('2N')
    e=n.count('3Y')
    f=n.count('3N')
    g=n.count('R')
    h=n.count('A')
    j=n.count('S')
    k=n.count('B')
    l=n.count('T')
    s=a+c*2+e*3+g+h+j+k-d-f-b-l
    print(s)