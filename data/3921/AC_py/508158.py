# coding=utf-8
n=int(input())
for i in range(n):
    a=str(input())
    rev=a[::-1]
    if a==rev:
        print("YES")
        
    else:
        print("NO")