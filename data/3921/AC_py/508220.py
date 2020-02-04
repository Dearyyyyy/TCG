# coding=utf-8
a=int(input())
for i in range(0,a):
    n=input()
    l=[]
    for j in n:
        l.append(j)
    l.reverse()
    z=''
    for k in l:
        z=z+k
    if z==n:
        print("YES")
    else:
        print("NO")