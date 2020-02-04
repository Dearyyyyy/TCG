# coding=utf-8
while True :
    q=[]
    def sui(n,star,end):
        global q
        if star >=end :
            q=q+n
        else :
            i=star
            for j in range(star ,end):
                n[j],n[i]=n[i],n[j]
                sui(n,star+1,end)
                n[j],n[i]=n[i],n[j]
    n=int(input())
    a=[]
    for i in range(1,n+1):
        a.append(i)
    sui(a,0,n)
    b=[]
    k=1
    for t in range(1,n+1):
        k=k*t
    for h in range(0,k):
        b.append(q[h*n:(h+1)*n])
    s=sorted(b)
    for r in s :
        for z in r :
            print(z,end=' ')
        print()