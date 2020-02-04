# coding=utf-8
while(True):
    a=int(input())
    i=0
    sum1=0
    x=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    while(i<a):
        
        b=input()
        if(x[ord(b[6])-65]!=-1):
            c=len(b)
            d=(ord(b[0])-48)*10+ord(b[1])-48
            e=(ord(b[3])-48)*10+ord(b[4])-48
            
            if(b[8]=="A"):
                sum1+=(d-18)*60+e+x[ord(b[6])-65]*20
                x[ord(b[6])-65]=-1
            else:
                x[ord(b[6])-65]+=1
        i+=1
    m=int(sum1/60)
    n=sum1%60
    if(m<10):
        print("0%d"%m,end="")
    else:
        print("%d"%m,end="")
    print(":",end="")
    if(n<10):
        print("0%d"%n,end="")
    else:
        print("%d"%n,end="")
    print()