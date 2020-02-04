# coding=utf-8
a=[[0]*3]*3
for i in range(3):
    a[i]=input().split()





temp=a[0][1]
a[0][1]=a[1][0]
a[1][0]=temp
temp=a[0][2]
a[0][2]=a[2][0]
a[2][0]=temp
temp=a[1][2]
a[1][2]=a[2][1]
a[2][1]=temp
for i in range(3):
    if i!=0:
        print()
    for j in range(3):
        print(a[i][j],end=' ')