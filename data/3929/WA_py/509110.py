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
        count=0
        if (c=='RE'or c=='WA' or c=='TLE' )and (j==1 or b==l[j-2] ):
           ## num+=1
            continue
        if  (c=='AC' and j==1) :
            time[3]+=int(a[4])
            time[2]+=int(a[3])
            if int(a[1])>=8 :
                time[1]+=(int(a[1])-8)
                time[0]=0
            elif int(a[1])<8:
                time[1]+=(int(a[1])+2)
                time[0]=0
        if c=='AC' and j>=2:
            for p in range(j-1):
                if l[p]==b:
                    count+=1
            if count==1:
                time[3] += int(a[4])
                time[2] += int(a[3])
                if int(a[1]) >= 8:
                    time[1] += (int(a[1]) - 8)
                    time[0] = 0
                elif int(a[1]) < 8:
                    time[1] += (int(a[1]) + 2)
                    time[0] = 0
    for q in range(n):
        f=1
        if ll[q]=='RE'or ll[q]=='WA' or ll[q]=='TLE':
            for x in range(q):
                if l[x]==l[q] and ll[x]=='AC':
                    f=0;
            if f==1:
                for o in range (q+1,n):
                    if l[q]==l[o] and ll[o]=='AC':
                        num+=1
                        break
    time[2]+=num*2
    if time[3]>=10:
        time[2]+=time[3]//10
        time[3]=time[3]%10
    if time[2]>=6:
        time[1]+=time[2]//6
        time[2]=time[2]%6
    print("%d%d:%d%d"%(time[0],time[1],time[2],time[3]))