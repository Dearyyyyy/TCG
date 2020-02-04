# coding=utf-8
n=int(input())
flag=0
for i in range(n):
    b=str(input())
    for j in range(len(b)):
        if(b[j]!=b[len(b)-1-j]):
            print("NO")
            break
    else:
        print("YES")