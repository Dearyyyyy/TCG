# coding=utf-8
while True :
    l=0
    a,b=input().split()
    c=a
    m=len(a)
    n=len(b)
    b=list(b)
    c=list(c)
    a=list(a)
    for k in range(m-1):
        j=0
        for i in range(1,m):
            c[j]=a[i]
            j=j+1
        c[j]=a[0]
        if c==b:
            l=1
    if l==1 :
        print("YES")
        l=0
    elif l==0 :
        print("NO")