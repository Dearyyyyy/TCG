# coding=utf-8
while(1):
    n=int(input())
    a=[]
    A=[]
    b=[]
    c=[]
    fs=e=q=0
    w=1
    hour=Hour=minute=Minute=fsh=fsm=sumh=summ=0
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
        e=0
        if(A[i]=='A'):
            for j in range(1,int(i/4)+1,1):
                if(w==1):
                    if(A[i-1]==A[i-1-(j*4)] and A[i-(j*4)]!='A'):
                        e+=1
                        w=1
                    if(A[i-1]!=A[i-1-(j*4)]):
                        e=e
                        w=1
                    if(A[i-1]==A[i-1-(j*4)] and A[i-(j*4)]=='A'):
                        w=0
                        
            fs+=20*e
    for i in range(3,len(A),4):
        if(A[i]=='A'):
            for j in range(1,int(i/4)+1,1):
                if(A[i-1]==A[i-1-(j*4)] and A[i-(j*4)]=='A'):
                    w=0
                else:
                    w=1
                if(w==0):
                    break
            if(w==1):
                hour=A[i-3]
                minute=A[i-2]
                q=1
                sumh=sumh+hour-18
                summ=summ+minute
                if(summ>59):
                    sumh+=1
                    summ-=60
    if(q==1):
        fsm=fs%60
        fsh=int(fs/60)
        Hour=sumh+fsh
        Minute=summ+fsm
        if(Minute>59):
            Hour+=1
            Minute=Minute-60
        elif(Minute<10 and Hour>=10):
            print(str(Hour)+":"+'0'+str(Minute))
        elif(Minute>=10 and Hour<10):
            print('0'+str(Hour)+":"+str(Minute))
        elif(Minute<10 and Hour<10):
            print('0'+str(Hour)+":"+'0'+str(Minute))
        else:
            print(str(Hour)+":"+str(Minute))
    else:
        print("00:00")