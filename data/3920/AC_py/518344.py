# coding=utf-8
n=int(input())
if (n//100)**3+(n%100//10)**3+(n%10)**3==n:
    print("YES")
else:
    print("NO")