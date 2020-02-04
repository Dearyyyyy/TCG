# coding=utf-8
a=int(input())
i=a//100
j=a//10-i*10
k=a%10
if a==i**3+j**3+k**3:
    print("YES")
else:
    print("NO")