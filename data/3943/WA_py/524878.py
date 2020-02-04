# coding=utf-8
COUNT=0
def perm(n,begin,end):
    global COUNT
    if begin>=end:
        for i in n:
            print(i,end=" ")
        print()
        COUNT +=1
    else:
        i=begin
        for num in range(begin,end):
            n[num],n[i]=n[i],n[num]
            perm(n,begin+1,end)
            n[num],n[i]=n[i],n[num]
while True:
    try:
        m=eval(input())
        if m == 0:
            break
        n=list(range(1,m))
        n.append(m)
        perm(n,0,len(n))
    except:
        break
        pass