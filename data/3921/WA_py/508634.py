# coding=utf-8
n=int(input())
for i in range(n):
    s1=list(input())
    s2=[0 for m in range(len(s1))]
    k=len(s1)-1
    for j in range(len(s1)):
        s2[jj]=s1[k]
        k=k-1
    t1='',join(s1)
    t2='',join(s2)
    if t1==t2:
        print('YES')
    else:
        print('NO')