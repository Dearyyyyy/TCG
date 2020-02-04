# coding=utf-8
line=[[0]*3]*3
line2=[[0]*3]*3
for i in range(3):
    line[i]=input().split()
temp=line[1][0]
line[0][1]=line[1][0]
line[1][0]=temp
temp=line[0][2]
line[0][2]=line[2][0]
line[2][0]=temp
temp=line[1][2]
line[1][2]=line[2][1]
line[2][1]=temp
for i in range(3):
    if i!=0:
        print()
    for j in range(3):
        print(line[i][j],end='')