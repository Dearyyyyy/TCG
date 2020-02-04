# coding=utf-8
Y='Y'
R='R'
S='S'
A='A'
B='B'
T='T'
while True:
    shots=0
    score=0
    rebound=0
    assists=0
    steal=0
    block=0
    turnover=0
    hits=0
    throws=0
    s=0
    a=input()
    for i in range (len(a)):
        if a[i]=='1'or a[i]=='2' or a[i]=='3':
            if a[i+1]==Y:
                score=score+int(a[i])
        if a[i]=='2' or a[i]=='3':
            shots=shots+1
            if a[i+1]==Y:
                hits=hits+1
        if a[i]=='1':
            throws=throws+1
            if a[i+1]==Y:
                s=s+1
        if a[i]==R:
            rebound=rebound+1
        if a[i]==A:
            assists=assists+1
        if a[i]==S:
            steal=steal+1
        if a[i]==B:
            block=block+1
        if a[i]==T:
            turnover=turnover+1
    e=(score+rebound+assists+steal+block)-(shots-hits)-(throws-s)-turnover
    print(e)