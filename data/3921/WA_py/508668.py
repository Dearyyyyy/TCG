# coding=utf-8
n=int(input())
flag=1
for i in range(n):
    str=input()
    a=len(str)
    for j in range(a):
       if str[j]!=str[a-1-j]:
           flag=0
    if flag==1:
        print("YES")
    else:
        print("NO")