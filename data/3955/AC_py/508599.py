# coding=utf-8
while(True):
    a=input()
    k=0
    for i in a:
        if(i==" "):
            break
        k=k+1
    b=len(a)
    k+=1
    c=k-1
    i=0
    flag2=1
    while(i<c):
        if((c)*2+1!=b):
            break
        m=0
        flag1=1
        j=0
        while(j<c):
            if(a[k+(j+i)%c]!=a[m]):
                flag1=0
                break
            m=m+1
            j=j+1
        if(flag1==1):
            print("Yes")
            flag2=0
            break
        i=i+1
    if(flag2==1):
        print("No")