# coding=utf-8
n = int(input)
for i in range(0,n):
    s1=input()
    s2=""
    for j in s1:
        s2=j+s2
    if s1==s2:
        print("YES")
    else :
        print("NO")