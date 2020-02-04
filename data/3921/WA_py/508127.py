# coding=utf-8
n=int(input())
for i in range (0,n):
    a=input()
    for j in range (0,len(a)//2):
        n=-1
        m=0
        if a[m]!=a[n]:
            print("NO")
            break
        n=n-1
        m=m+1
    else:
        print("YES")