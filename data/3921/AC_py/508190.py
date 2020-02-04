# coding=utf-8
n=int(input())
for i in range(n):
    a=input()
    if a == a[::-1]:
        print("YES")
    else:
        print("NO")