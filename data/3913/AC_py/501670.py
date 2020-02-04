# coding=utf-8
b=[]
for _ in range(3):
    b.append(list(map(int,input().rstrip().split())))
t=0
for i in range(3):
    for j in range(i):
        a=b[i][j]
        b[i][j]=b[j][i]
        b[j][i]=a
for i in range(3):
    for j in range(3):
        print(b[i][j],end=' ')
    print()