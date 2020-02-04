# coding=utf-8
while True :
    n=eval(input())
    num=0
    time=[0,0,0,0]
    l=[]
    ll=[]
    j=0
    for i in range(n):
        a,b,c=input().split()
        l.append(b)
        ll.append(c)
        j+=1
        if c=='RE'or c=='WA' or c=='TLE':
            num+=1
            continue
        if (c=='AC' and b==l[j-2]) or (c=='AC' and j==1) :
            time[3]+=int(a[4])
            time[2]+=int(a[3])+num*2
            if int(a[1])>=8 :
                time[1]+=(int(a[1])-8)
                time[0]=0
            elif int(a[1])<8:
                time[1]+=(int(a[1])+2)
                time[0]=0
    if time[3]>=10:
        time[2]+=time[3]//10
        time[3]=time[3]%10
    if time[2]>=6:
        time[1]+=time[2]//6
        time[1]=time[2]%6
    print("%d%d:%d%d"%(time[0],time[1],time[2],time[3]))