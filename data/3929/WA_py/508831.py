# coding=utf-8
while True:
    s1=0
    s2=0
    k={}
    c=''
    c2=''
    n=int(input())
    for i in range(n):
        a1,a2,a3=input().split(" ")
        if a2 not in c:
            k['a2']=0
            c=c+a2
        if a3!='AC':
            k['a2']=k['a2']+1
        if a3=='AC' and a2 not in c2:
            s1=s1+int(a1[0:2])-18
            s2=s2+int(a1[3:])+20*k['a2']
            c2=c2+a2
    s1=s1+(s2/60)
    s2=s2%60
    print("%02d:%02d"%(s1,s2))