# coding=utf-8
while True:
    sc=0
    re=0
    ass=0
    st=0
    bl=0
    nus=0
    nuh=0
    nuf=0
    snuf=0
    to=0
    a=input()
    i=0
    while i in range(len(a)):
        if a[i]=='R':
            re+=1
        elif a[i]=='A':
            ass+=1
        elif a[i]=='S':
            st+=1
        elif a[i]=='B':
            bl+=1
        elif a[i]=='T':
            to+=1
        elif a[i]=='1':
            nuf+=1
            i+=1
            if a[i]=='Y':
                snuf+=1
                sc+=1
        elif a[i]=='2':
            nus+=1
            i+=1
            if a[i]=='Y':
                nuh+=1
                sc+=2
        elif a[i]=='3':
            nus+=1
            i+=1
            if a[i]=='Y':
                nuh+=1
                sc+=3
        i+=1
    print((sc+re+ass+st+bl)-(nus-nuh)-(nuf-snuf)-to)