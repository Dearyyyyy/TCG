# coding=utf-8
while True:
    n=int(input())
    p=0
    tm=[0 for j in range(26)]
    tp1=[0 for l in range(26)]
    flg=0
    for i in range(n):
        h=['0','0']
        m=['0','0']
        re=['0','0']
        tp=[0 for l in range(26)]
        p0=0
        p1=0
        p2=0
        th=0
        a=list(input())
        h[0]=a[0]
        h[1]=a[1]
        m[0]=a[3]
        m[1]=a[4]
        re[0]=a[8]
        re[1]=a[9]
        th=a[6]
        tm[ord(th)-65]+=1
        tp1[ord(th)-65]=(int(h[0])*10+int(h[1])-18)*60\
            +int(m[0])*10+int(m[1])
        if re[0]=='A' and re[1]=='C':
            tp[ord(th)-65]+=(int(h[0])*10+int(h[1])-18)*60\
            +int(m[0])*10+int(m[1])\
            +(tm[ord(th)-65]-1)*20
            flg=1

        for k in range(26):
            p+=tp[k]
        for k in range(26):
            p0+=tp1[k]
    if flg==1:
        p1=p%60
        print("%02d:"%int(p/60)+"%02d"%p1)
    else:
        p1=p0%60
        print("%02d:"%int(p0/60)+"%02d"%p1)