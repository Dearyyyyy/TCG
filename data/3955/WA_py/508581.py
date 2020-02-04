# coding=utf-8
while True:
    a,b = input().split()
    c = a[len(a)-1]+a[0:len(a)-1]
    if b==c:
        print('Yes')
    else:
        print('No')