# coding=utf-8
while(True):
    a=input()
    b=len(a)
    i=1
    sum1=0
    while(i<b):
        if(a[i]=='Y'):
            sum1+=ord(a[i-1])-48
        i=i+2
    print(sum1)