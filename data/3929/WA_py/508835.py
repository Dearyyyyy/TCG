# coding=utf-8
while True:
    a=int(input())
    t='AC'
    f1='WA'
    f2='RE'
    f3='TLE'
    k=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    h=0
    m=0
    for i in range(0,a):
        s=input()
        if t in s:
            h=h+(ord(s[0])-48)*10+ord(s[1])-48
            m=m+(ord(s[3])-48)*10+ord(s[4])-48
            for j in k:
                if j==s[6]:
                    m=m+20
        elif f1 in s or f2 in s or f3 in s:
            k[i]=s[6]
    h=h+m//60
    m=m%60
    if h-18<10:
        print('0%d:%d'%(h-18,m))
    else:
        print('%d:%d'%(h-18,m))