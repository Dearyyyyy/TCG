# coding=utf-8
while 1:
    x,y=map(int,input().split())
    if(y==0):
        print("error")
    else:
        if((x/y-x//y)>=0.5):
            print(x//y+1)
        else:
            print(x//y)