# coding=utf-8
num=[[0]*3]*3
for i in range(0,3):
    num[i]=input().split(" ")
for i in range(0,3):
    for j in range(0,i):
        a=num[i][j]
        num[i][j]=num[j][i]
        num[j][i]=a
for i in range(0,3):
    print(num[0][i],end=' ')
print('\n',end='')
for i in range(0,3):
    print(num[1][i],end=' ')
print('\n',end='')
for i in range(0,3):
    print(num[2][i],end=' ')