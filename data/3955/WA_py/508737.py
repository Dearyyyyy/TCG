# coding=utf-8
while True:
    a,b=input().split()
    for i in range(len(a)):
        d=a[1:len(a)]+a[0]
        a=d
        if a==b:
            flag=1
            break
        else:
            flag=0
    if flag==1:
        print('YES')
    else:
        print('NO')