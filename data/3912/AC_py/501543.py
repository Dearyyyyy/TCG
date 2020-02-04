# coding=utf-8
a=float(input())
i=2
flag=0
if a<3:
    flag=0
else :
    while i<=a**(0.5):
        if a%i==0:
            flag=0
            break
        else:
            flag=1
        i+=1
if flag==0:
    print('not prime')
else :
    print('prime')