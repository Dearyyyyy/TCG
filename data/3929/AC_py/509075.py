# coding=utf-8
while True:
    l=[]
    l=[0]*26
    lwrong=[]
    lwrong=[0]*26
    h=0
    minute=0
    boss=0
    temp=0
    n=int(input())
    for i in range(n):
        a,b,c=input().split()
        if c=='AC':
            if l[ord(b)-65]==0:
                l[ord(b)-65]=1
                h=h+int(a[0:2])-18
                minute=minute+int(a[3:5])
        else:
            if l[ord(b)-65]==0:
                lwrong[ord(b)-65]+=1
    for i in range(26):
        if l[i]==1:
            minute+=lwrong[i]*20
    if minute>=60:
        temp=minute//60
        minute=minute-60*temp
        h=h+temp
    if h>60:
        temp=h//60
        h=h-60*temp
        boss=boss+temp
    if boss!=0:
            print("%02d:%02d:%02d" % (boss,h,minute))
    if boss==0:
            print("%02d:%02d" % (h,minute))