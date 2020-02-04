# coding=utf-8
while True :
    n=eval(input())
    num=0
    time=[0,0,0,0]
    for i in range(n):
        a,b,c=input().split()
        if c=='RE':
            num+=1
        elif c=='AC':
            time[3]+=int(a[4])
            time[2]+=int(a[3])
            if int(a[1])>=8 :
                time[1]+=(int(a[1])-8)
                time[0]=0
            elif int(a[1])<8:
                time[1]+=(int(a[1])+2)
                time[0]=0
    time[2]+=num*2
    if time[3]>=10:
        time[2]+=time[3]//10
        time[3]=time[3]%10
    if time[2]>=6:
        time[1]+=time[2]//6
        time[1]=time[2]%6
    print("%d%d:%d%d"%(time[0],time[1],time[2],time[3]))