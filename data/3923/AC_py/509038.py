# coding=utf-8
import string
while  True:
    a=input()
    a1=a.count('1Y')
    a2=a.count('1N')
    a3=a.count('2Y')
    a4=a.count('2N')
    a5=a.count('3Y')
    a6=a.count('3N')
    a7=a.count('R')
    a8=a.count('A')
    a9=a.count('S')
    b=a.count('B')
    c=a.count('T')
    s=a1+a3*2+a5*3+a7+a8+a9+b-a4-a6-a2-c
    print(s)