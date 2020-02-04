# coding=utf-8
def res(n):
    flag = 1
    if n==0 or n==1:
        print("not prime")
    elif n==2:
        print("prime")
    else:
        for i in range(2,n):
            if (n%i)==0:
                
                flag=0
                break

        if flag==1:
            print("prime")
        else:
             print("not prime")
n=eval(input())
res(n)