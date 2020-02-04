# coding=utf-8
while True:
    try:
        a,b=input().split()
        x=len(a)
        if a==b:
            print('Yes')
        else:
            for i in range(0,x):
                m=a[::-1]
                n=m[0]
                a=a[:-1]
                a=a.rjust(x,n)
                if a==b:
                    print('Yes')
                    break
            if i==x-1:
                print('No')
    except:
         break