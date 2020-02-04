# coding=utf-8
while True:
    a,b=map(int,input().split())
    if b==0:
        print("error")
        continue
    c=a/b
    d=a//b
    if c%1>0.499999:
        d=d+1
    print(d)