# coding=utf-8
while True:
    s1=0
    s2=0
    k=''
    c=0
    n=int(input())
    for i in range(n):
        a1,a2,a3=input().split(" ")
        if i==0:
            k=a2
        if a2==k and a3!='AC':
            c=c+1
        elif a2!=k:
            c=0
        k=a2
        if a3=='AC':
            s1=s1+int(a1[0:2])-18
            s2=s2+int(a1[3:])+20*c
    s1=s1+(s2/60)
    s2=s2%60
    print("%02d:%d"%(s1,s2))