# coding=utf-8
n=int(input())
for i in range(n):
    m=str(input())
    n=0
    n=m[::-1]
    if(n==m):
        print("YES")
    else:
        print("NO")