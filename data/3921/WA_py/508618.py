# coding=utf-8
n=int(input())
for i in range(n):
    s1=list(input())
    s2=[0 for a in range(len(s1))]
    t=len(s1)-1
    for j in range(len(s1)):
        s2[j]=s1[t]
        t=t-1
    x=''.join(s1)
    y='',join(s2)
    if x==y:
        print('YES')
    else:
        print('NO')