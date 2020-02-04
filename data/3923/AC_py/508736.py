# coding=utf-8
while True:
    s1=input()
    a1=s1.count('1Y')
    a2 = s1.count('1N')
    a3 = s1.count('2Y')
    a4 = s1.count('2N')
    a5 = s1.count('3Y')
    a6 = s1.count('3N')
    a7 = s1.count('R')
    a8 = s1.count('A')
    a9 = s1.count('S')
    a10 = s1.count('B')
    a11 = s1.count('T')
    s=(a1+a3*2+a5*3+a7+a8+a9+a10)-(a4+a6)-a2-a11
    print(s)