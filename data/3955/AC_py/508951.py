# coding=utf-8
while True:
    s=1
    a,b=input().split()
    for i in range(len(a)):
        a=a[-1]+a[:-1]
        if a==b:
            print('Yes')
            s=0
    if s==1:
        print('No')