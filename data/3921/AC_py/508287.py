# coding=utf-8
a=int(input())
for i in range(0,a):
    s=str(input())
    t=s[::-1]
    if s==t:
        print("YES")
    else:
        print("NO")