# coding=utf-8
a=int(input())
j=0
while(j<a):
    strr=input()
    b=len(strr)
    i=0
    flag=0
    while(i<int(b/2)):
        if(strr[i]!=strr[b-1-i]):
            flag=1
        i=i+1
    if(flag==0):
        print("YES")
    else:
        print("NO")
    j=j+1