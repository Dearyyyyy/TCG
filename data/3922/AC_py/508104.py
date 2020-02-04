# coding=utf-8
while True:
    m,n=input().split()
    m=int(m)
    n=int(n)
    if n==0:
        print("error")
    else:
        c=m/n
        d=m//n
        if (c-d)*2>=1:
            
            
            print(d+1)
        else:
            
            print(d)