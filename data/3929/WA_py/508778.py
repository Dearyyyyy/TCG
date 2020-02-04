# coding=utf-8
x=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while(True):
    a=int(input())
    i=0
    sum1=0
    k=0
    while(i<a):
        
        b=input()
        if(ord(b[6])-65!=-1):
            c=len(b)
            d=(ord(b[0])-48)*10+ord(b[1])-48
            e=(ord(b[3])-48)*10+ord(b[4])-48
            x[ord(b[6])-65]+=1
            if(b[8]=="A"):
                sum1+=(d-18)*60+e+k*20
                x[ord(b[6])-65]=-1
            else:
                k+=1
        i+=1
    print("0%d:%d"%(int(sum1/60),sum1%60))