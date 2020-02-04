# coding=utf-8
num=int(input())
for i in range(num):
    str=input()
    if str==str[::-1]:
        print("YES")
    else:
        print("NO")