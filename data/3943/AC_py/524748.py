# coding=utf-8
while True:
    q=[]
    def perm(n,begin,end):
        global q
        if begin >= end:
            q+=n
        else:
            i=begin
            for num in range(begin,end):
                n[num],n[i]=n[i],n[num]
                perm(n,begin+1,end)
                n[num],n[i]=n[i],n[num]
    n=int(input())
    a=[]
    for i in range(1,n+1):
        a.append(i)
    perm(a,0,n)
    b=[]
    temp=1
    for w in range(1,n+1):
        temp *= w
    for j in range(0,temp):
        b.append(q[j*n:j*n+n])
    ss=sorted(b)
    for r in ss:
        for c in r:
            print(c,end=" ")
        print()