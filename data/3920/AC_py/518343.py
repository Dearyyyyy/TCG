# coding=utf-8
n=int(input())
m=n%10
i=(n//10)%10
j=n//100
if m**3+i**3+j**3==n:
    print("YES")
else:
    print("NO")