# coding=utf-8
while True :
    a,b=input().split()
    a,b=int(a),int(b)
    if(b==0):
        print("error")
    else :
        c=a//b
        d=a/b-c
        if d*2>=1 :
            c=c+1
            print(c)
        else :
            print(c)