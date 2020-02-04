# coding=utf-8
a = []
b = []
for i in range(3):
	a.append(list(map(int, input().rstrip().split())))
# for i in a:
#     b.append(i)
for i in range(3):
    for j in range(3):
        b.append(a[j][i])
# for i in range(0,3):
#     for j in range(0,3):
#         b[j][i]=a[i][j]
# print(a)
# print(b)
for i in range(9):
    # print(b[i],end=" ")
    if (i+1)%3==0:
        print(b[i])
    else:
        print(b[i],end=" ")