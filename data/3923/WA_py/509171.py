# coding=utf-8
while True:
    ay=0
    an=0
    by=0
    bn=0
    cy=0
    cn=0
    r=0
    a=0
    s=0
    b=0
    t=0
    g=input()
    ay=g.count("1Y")
    an=g.count("1N")
    by=g.count("2Y")
    bn=g.count("2N")
    cy=g.count("3Y")
    cn=g.count("3N")
    r=g.count("R")
    a=g.count("A")
    s=g.count("S")
    b=g.count("B")
    t=g.count("T")
    score=ay+by*2+cy*3
    nshots=by+bn+cy+cn
    nhits=by+cy
    nfreethrows=ay+an
    Thensuccessfulfreethrows=ayvalue=(score+r+a+s+b)-(nshots-nhits)-(nfreethrows-Thensuccessfulfreethrows)-t
    print(value)