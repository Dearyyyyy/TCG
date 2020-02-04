# coding=utf-8
while True:
    s=[]
    k=n=n1=score=0
    s=[str(i) for i in input()]
    for i in s:
        if i=='1':
            k=1
            n+=1
        if i=='2':
            k=2
            n+=1
        if i=='3':
            k=3
            n+=1
        if i=='Y':
            score+=k
            n1+=1
        if i=='R':
            score+=1
        if i=='A':
            score+=1
        if i=='S':
            score+=1
        if i=='B':
            score+=1
        if i=='T':
            score-=1
    print(score-n+n1)