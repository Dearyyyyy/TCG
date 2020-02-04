# coding=utf-8
def perm(n,begin,end):
    if begin>=end:
        print(*n)
    else:
        i=begin
        for num in range(begin,end):
            n[num],n[i]=n[i],n[num]
            perm(n,begin+1,end)
            n[num],n[i]=n[i],n[num]
while True:
    a=int(input())
    if(a==0):
        break
    n=[]
    for i in range(1,a+1):
        n.append(i)
    perm(n,0,len(n))