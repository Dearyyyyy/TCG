# coding=utf-8
while(1):
    a=[]
    A=B=C=D=T=0
    a=input()
    n=len(a)
    for i in range(n):
        if(a[i]=='1'):
            if(a[i+1]=='Y'):
                A+=1
            if(a[i+1]=='N'):
                D+=1
        if(a[i]=='2'):
            if(a[i+1]=='Y'):
                A+=2
            if(a[i+1]=='N'):
                C+=1
        if(a[i]=='3'):
            if(a[i+1]=='Y'):
                A+=3
            if(a[i+1]=='N'):
                C+=1
        if(a[i]=='R' or a[i]=='A' or a[i]=='S' or a[i]=='B'):
            B+=1
        if(a[i]=='T'):
            T+=1
    print((A+B)-C-D-T)