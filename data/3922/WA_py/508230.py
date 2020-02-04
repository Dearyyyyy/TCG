# coding=utf-8
while True:
    a,b=map(int,input().split())
    if(b==0):
        print("ERROR")
    else:
        if((a/b)>=0.5):
            print(a//b+1)
        else:
            print(a//b)