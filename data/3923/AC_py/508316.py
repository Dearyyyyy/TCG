# coding=utf-8
while True :
    n=input()
    num1=0
    num2=0
    num3=0
    numR=0
    num1Y=0
    num2Y=0
    num3Y=0
    numT=0
    score=0
    for i in range(len(n)):
        if n[i]=='1':
            num1+=1
            if n[i+1]=='Y':
                num1Y+=1
        elif n[i]=='2':
            num2+=1
            if n[i+1]=='Y':
                num2Y+=1
        elif n[i]=='3':
            num3+=1
            if n[i+1]=="Y":
                num3Y+=1
        elif n[i]=='R' or n[i]=='A' or n[i]=='S' or n[i]=="B":
            numR+=1
        elif n[i]=='T':
            numT+=1
    score=num1Y+num2Y*2+num3Y*3
    XL=(score+numR)-(num2+num3-num2Y-num3Y)-(num1-num1Y)-numT
    print(XL)