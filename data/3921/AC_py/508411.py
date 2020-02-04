# coding=utf-8
n=int(input())
for i in range(n):
    a=input()
    s=a[::-1]
    if a==s:
        print("YES")
    else:
        print("NO")