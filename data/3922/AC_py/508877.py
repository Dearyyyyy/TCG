# coding=utf-8
while True:
    a,b=input().split()
    a=float(a)
    b=float(b)
    if(b==0):
        print("error")
    else:
        c=a/b
        if(c-int(c)>=0.5):
            result=int(c)+1
            print(result)
        else:
            result=int(c)
            print(result)