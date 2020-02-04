# coding=utf-8
a=int(input())
flag =0
for i in range(1,a) :
    if a%i==0 :
        flag+=1
if flag>1 :
        print("prime")
else :
        print("not prime")