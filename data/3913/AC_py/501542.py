# coding=utf-8
list1=[]
k=0
for i in range(3):
    list1.append(list(map(int,input().rstrip().split())))
temp=list1[0][1]
list1[0][1]=list1[1][0]
list1[1][0]=temp

temp=list1[0][2]
list1[0][2]=list1[2][0]
list1[2][0]=temp

temp=list1[1][2]
list1[1][2]=list1[2][1]
list1[2][1]=temp
for j in list1[0]:
    print(j,end=' ')
print()
for j in list1[1]:
    print(j,end=' ')
print()
for j in list1[2]:
    print(j,end=' ')