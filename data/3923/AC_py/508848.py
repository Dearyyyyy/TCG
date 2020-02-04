# coding=utf-8
while True:
    a=input()
    t=0
    throw=0
    shoot=0
    efficient=0
    for i in a:
        if i=='R' or i=='A' or i=='S' or i=='B':
            t+=1
        elif i=='T':
            t-=1
    for i in range(0,len(a),2):
        if a[i:i+2]=='1N' or a[i:i+2]=='2N' or a[i:i+2]=='3N' :
            throw+=1
        elif a[i:i+2]=='1Y' :
            throw+=1
            shoot+=1
            t+=1
        elif a[i:i+2]=='2Y' :
            throw+=1
            t+=2
            shoot+=1
        elif a[i:i+2]=='3Y' :
            throw+=1
            t+=3
            shoot+=1
    efficient=t-throw+shoot
    print(efficient)