# coding=utf-8
def pd(a,b):
    c=a;
    t=a[len(a)-1]+a[1:len(a)-1]+a[0]

    if(b==t):
        return 1
    else:
        return 0
a,b=input().split()
if(pd(a,b)):
    print('YES')
else:
    print('NO')