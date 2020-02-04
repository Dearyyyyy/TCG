# coding=utf-8
while(True):
    a,b=map(int,input().split())
    if(b==0):
        print("error")
    else:
        if(a%b>=b/2):
            print(int(a/b)+1)
        else:
            print(int(a/b))