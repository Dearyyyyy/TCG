# coding=utf-8
a=[]
for _ in range(3):
    a.append(list(map(int,input().rstrip().split())))
t=0
for i in range(3):
    for j in range(i):
        t=a[i][j]
        a[i][j]=a[j][i]
        a[j][i]=t
for i in range(3):
    for j in range(3):
        print(a[i][j],end=' ')
    print()