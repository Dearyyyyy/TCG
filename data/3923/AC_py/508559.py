# coding=utf-8

while True:
    s=[]
    s=[str(i) for i in input()]
    flag=0
    num=num2=num3=num4=score=0
    for i in s:
        if i=='1':
            flag=1
            num=num+1
        if i=='2':
            flag=2
            num=num+1
        if i=='3':
            flag=3
            num=num+1
        if flag!=0:
            if i=='Y':
                score=score+flag
                num4=num4+1
                flag=0
        if i=='R':
            num2=num2+1
        if i=='A':
            num2=num2+1
        if i=='S':
            num2=num2+1
        if i=='B':
            num2=num2+1
        if i=='T':
            num3=num3+1
    print(score+num2-num+num4-num3)