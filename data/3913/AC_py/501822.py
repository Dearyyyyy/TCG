# coding=utf-8
List=[[],[],[]]
for i in range (3):
    List[i]=list(input().split())
for m in range(3):
    for n in range (3):
        (List[m])[n]=int((List[m])[n])
for m in range(3):
    for n in range(1+m,3):
        t=(List[m])[n]
        (List[m])[n] = (List[n])[m]
        (List[n])[m]=t
for q in range(3):
    for p in range(3):
        print((List[q])[p],end=' ')
    print()