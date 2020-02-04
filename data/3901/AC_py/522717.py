# coding=utf-8
n=int(input())
x=1
while(1):
    X=x
    for i in range(n-1):
        x=(x/2)-1
    if(x==1):
        print(X)
        break
    else:
        x=X+1