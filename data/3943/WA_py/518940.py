# coding=utf-8
q=[]
def order(n,begin,end):
    global q
    if begin>=end:
        q+=n
    else :
        i=begin
        for num in range(begin,end):
            n[num],n[i]=n[i],n[num]
            order(n,begin+1,end)
            n[num],n[i]=n[i],n[num]
while True :
    n=int(input())
    if n==0:
        break
    list1=[]
    for i in range(1,n+1):
        list1.append(i)
    order(list1,0,n)
    list2=[]
    temp=1
    for h in range(1,n+1):
        temp*=h
    for j in range(0,temp):
        list2.append(q[j*n:j*n+n])
    s=sorted(list2)
    for r in s :
        for c in r:
            print(c,end=' ')
        print()