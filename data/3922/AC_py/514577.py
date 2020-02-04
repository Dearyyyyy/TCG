# coding=utf-8
while(1):
    a,b=map(int,input().split())
    if(b==0):
        print("error")
    else:
        c=a/b
        x=c*10
        d=x%10
        if(d<5):
            c=int(c)
            print(c)
        if(d<10 and d>=5):
            c=int(c+1)
            print(c)