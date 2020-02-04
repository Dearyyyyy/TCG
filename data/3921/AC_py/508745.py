# coding=utf-8
n=input()
n=int(n)
while True:
    i=1
    if i<=n:
        a=input()
        l=[]
        m=[]
        for z in str(a):
            l.append(z)
            m.append(z)
        i+=1
        l.reverse()
        if l == m:
            print("YES")
        else:
            print("NO")
    else:
        break