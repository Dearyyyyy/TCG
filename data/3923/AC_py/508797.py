# coding=utf-8
while True:
    a=input()
    l=len(a)
    s,f,e,t=(0,0,0,0)
    for i in range(l):
        if a[i]=='1':
            if a[i+1]=='Y':
                s=s+1
            elif a[i+1]=='N':
                f=f+1
        elif a[i]=='2':
            if a[i+1]=='Y':
                s=s+2
            elif a[i+1]=='N':
                f=f+1
        elif a[i]=='3':
            if a[i+1]=='Y':
                s=s+3
            elif a[i+1]=='N':
                f=f+1
        elif a[i]=='R' or a[i]=='A' or a[i]=='S' or a[i]=='B':
            e=e+1
        elif a[i]=='T':
            t=t+1
    print(s+e-f-t)