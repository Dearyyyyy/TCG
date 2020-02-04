# coding=utf-8
l = [[],[],[]]
for i in range(3):
    l[i]=list(input().split())
for m in range(3):
    for n in range(3):
        l[m][n]=int(l[m][n])
for n in range(3):
    for m in range(3):
        print("%d"%l[m][n],end = ' ')
    print()