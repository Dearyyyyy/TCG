a=[0]*15
def p(site,n):
    if site==n:
        for i in range(0, n-1, 1):
            print a[i],
        print "%i%s"%(a[n-1],' ')
        return
    for i in range(1,n+1,1):
        bl=1
        for t in range(0,site,1):
            if i==a[t]:
                bl=0
                break
        if bl:
            a[site]=i
            p(site+1,n)

while True:
    q=input()
    if q==0:
        break
    for i in range(0,q,1):
        a[i]=i+1
    p(0,q)