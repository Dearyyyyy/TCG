# coding=utf-8
A = []
for i in range(3):
    A.append((input().split(' ')))
main0 = 0
by0 = 0
temp = []
for i in range(3):
    temp.append([])
    for j in range(3):
        temp[i].append(A[j][i])
for i in range(3):
    print(' '.join(temp[i]))