# coding=utf-8
def money(n:int)->int:
    list=[]
    l=0
    i=0
    q=n%10
    n=n-q
    if q>=5:
        q=q-5
        i=1##5元
        if q>=2:
            l=q//2##2元
            o=q-2*l##1元
        else:
            o=q##1yuan
    elif q>=2 and q<5:
        i=0
        l=q//2
        o=q-2*l
    else:
        i=0
        l=0
        o=q
    w=n//100##100元
    n=n-w*100
    if n>=50:
        t=1##50yuan
        n=n-50
        if n>=20:
            y=n//20##20yuan
            n=(n-y*20)/10
            u=n##10yuan
    elif n>=20 and n<50:
        t=0
        y=n//20
        u=(n-y*20)/10
    else:
        t=0
        y=0
        u=n/10
    list.append(o)
    list.append(int(l))
    list.append(i)
    list.append(int(u))
    list.append(y)
    list.append(t)
    list.append(w)
    return list

n=eval(input())
while n>0:
    c=eval(input())
    h=money(int(c))
    for f in range(len(h)):
        print(h[f],end=" ")
    print()
    n-=1