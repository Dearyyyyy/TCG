# coding=utf-8

numList1 = []
for i in range(3):
    b = []
    b = list(input().split())
    numList1.append(b)

for i in range(3):
    for j in range(3):
        print(numList1[j][i], end=' ')
    print()