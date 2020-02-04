# coding=utf-8
while(1):
    a,b=map(int,input().split())
    if(b==0):
        print("error")
    else:
        c=a/b
        d=c*10
        if(d<5):
            c=int(c)
            print(c)
        else:
            c=int(c+1)
            print(c)