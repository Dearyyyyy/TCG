# coding=utf-8
while True:
    s=input()
    Y1=s.count("1Y")
    N1=s.count("1N")
    Y2=s.count("2Y")
    N2=s.count("2N")
    Y3=s.count("3Y")
    N3=s.count("3N")
    R=s.count("R")
    A=s.count("A")
    S=s.count("S")
    B=s.count("B")
    T=s.count("T")
    TOTAL=(Y1+2*Y2+3*Y3+S+B+A+R)-(N2+N3)-N1-T
    print(TOTAL)