# coding=utf-8
while True:
    a=int(input())
    bb=0
    b=a
    while b!=0:
        bb+=(b%10)**3
        b = b // 10
    if bb==a:
        print("YES")
    else:
        print("NO")