# coding=utf-8
while True:
    m=int(input())
    bb=0
    b=m
    while b!=0:
        bb+=(b%10)**3
        b = b // 10
    if bb==m:
        print("YES")
    else:
        print("NO")