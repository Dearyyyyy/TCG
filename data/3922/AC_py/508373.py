# coding=utf-8
while True:
    n=input().split()
    a=float(n[0])
    b=float(n[1])
    if b==0:
        print('error')
    else:
        m=a/b
        p=a//b
        if m-p>0.49999:
            print(int(p+1))
        else :
            print(int(p))