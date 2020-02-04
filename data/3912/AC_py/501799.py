# coding=utf-8
a=int(input())
if a<=1 :
    print("not prime")
elif a==2 :
        print("prime")
else :
        for i in range(2,a):
            if a%i ==0:
                break;
        if i==a-1 :
            print("prime")
        else :
            print("not prime ")