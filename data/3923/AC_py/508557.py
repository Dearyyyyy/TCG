# coding=utf-8
while True:
    s=[]
    k=num1=num=score=0
    s=[str(i) for i in input()]
    for i in s:
        if i=='1':
            k=1
            num=num+1
        if i=='2':
            k=2
            num=num+1
        if i=='3':
            k=3
            num=num+1
        if i=='Y':
            score=score+k
            num1=num1+1
            k==0
        if i=='R':
            score=score+1
        if i=='A':
            score=score+1
        if i=='S':
            score=score+1
        if i=='B':
            score=score+1
        if i=='T':
            score=score-1
    print(score-num+num1)