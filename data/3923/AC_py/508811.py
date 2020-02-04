# coding=utf-8
while True:
    y1=0
    n1=0
    y2=0
    n2=0
    y3=0
    n3=0
    r=0
    a=0
    s=0
    b=0
    t=0
    str=input()
    y1=str.count("1Y")
    n1=str.count("1N")
    y2=str.count("2Y")
    n2=str.count("2N")
    y3=str.count("3Y")
    n3=str.count("3N")
    r=str.count("R")
    a=str.count("A")
    s=str.count("S")
    b=str.count("B")
    t=str.count("T")
    x=y1+2*y2+3*y3+r+a+s+b-(n2+n3)-n1-t
    print(x)