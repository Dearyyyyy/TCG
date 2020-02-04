# coding=utf-8
while True:
    a,b = input().split()
    for i in range (len(a)):
        c = a[i:]+a[:i]
    if c == b:
        print('Yes')
    else:
        print('No')