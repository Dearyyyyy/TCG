# coding=utf-8
a=input()
a=int(a)
if a<2:
    print("not prime")
if a==2:
    print("prime")
if a>=3:
    i=2
    while i*i<a:
        if a%i==0:
            print("not prime")
            break
        i+=1
    else:
        print("prime")