# coding=utf-8
a=int(input())
flag=0
if a>1:
    for i in range(2,a-1):
        if (a%i)==0:
            print("not prime")
            flag=1
            break
    if flag==0:
        print("prime")
else :
    print("not prime")