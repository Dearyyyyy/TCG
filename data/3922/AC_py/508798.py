# coding=utf-8
while True:
    a,b=input().split()
    a,b=int(a),int(b)
    if b==0:
        print("error")
    if b>0 or b<0:
        c=a/b
        d=a//b
        e=c-d
        if e>=0.5:
            d=d+1
            print(d)
        elif e<0.5:
            print(d)