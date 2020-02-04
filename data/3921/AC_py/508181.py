# coding=utf-8
n = int(input())
for i in range(n):
    k = input()
    if k == k[::-1]:
        print("YES")
    else:
        print("NO")