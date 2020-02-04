# coding=utf-8
a=[]
def order(n,start,end):
    global a
    if begin>=end:
        a+=n
    else :
        i=start
        for num in range(start,end):
            n[num],n[i]=n[i],n[num]
            order(n,start+1,end)
            n[num],n[i]=n[i],n[num]
while True :
    a=[]
    temp=1
    n=int(input())
    if n==0:
        break
    list1=[]
    for i in range(1,n+1):
        list1.append(i)
    order(list1,0,n)
    list2=[]
    for h in range(1,n+1):
        temp*=h
    for j in range(0,temp):
        list2.append(a[j*n:j*n+n])
    s=sorted(list2)
    for r in s :
        for b in r:
            print(b,end=' ')
        print()