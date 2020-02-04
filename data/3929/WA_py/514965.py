# coding=utf-8
while(1):
    n=int(input())
    a=[]
    A=[]
    B=[]
    b=[]
    c=[]
    fs=e=0
    hour=Hour=minute=Minute=fsh=fsm=0
    for i in range(n):
        a,b,c=input().split()
        list(a)
        h=int(a[0])*10+int(a[1])
        m=int(a[3])*10+int(a[4])
        A.append(h)
        A.append(m)
        A.append(b[0])
        A.append(c[0])
    for i in range(3,len(A),4):
        e+=1
        if(A[i]=='A' and A[i-1]==A[i-5]):
            fs+=20*(e-1)
        if(A[i-1]!=A[i-5]):
            e=1
    B=A[::-1]
    for i in range(0,len(B),4):
        if(B[i]=='A'):
            hour=int(B[i+3])
            minute=int(B[i+2])
            break
    fsm=fs%60
    fsh=int(fs/60)
    Hour=hour-18+fsh
    Minute=minute+fsm
    if(Minute>59):
        Hour+=1
        Minute=Minute-60
    elif(Minute<10 and Hour>=10):
        print(str(Hour)+":"+'0'+str(Minute))
    elif(Minute>=10 and Hour<10):
        print('0'+str(Hour)+":"+str(Minute))
    elif(Minute<10 and Hour<0):
        print('0'+str(Hour)+":"+'0'+str(Minute))