# coding=utf-8
while 1:
    Y1=0
    N1=0
    Y2=0
    N2=0
    Y3=0
    N3=0
    R=0
    A=0
    S=0
    B=0
    T=0
    l=input()
    Y1=l.count('1Y')
    N1=l.count('1N')
    Y2=l.count('2Y')
    N2=l.count('2N')
    Y3=l.count('3Y')
    N3=l.count('3N')
    R=l.count('R')
    A=l.count('A')
    S=l.count('S')
    B=l.count('B')
    T=l.count('T')
    s=0
    s=(Y1+Y2 *2+Y3 *3+R+S+B+A)-(N2+N3)-(N1)-T
    print(s)