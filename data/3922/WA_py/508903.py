# coding=utf-8
while True:
    a,b=input().split(' ')
    a=int(a)
    b=int(b)
    if b==0:
        print("error")
    else:
        c=a/b
        d=a//b
        if c<1:
            if 10*c>=5:
                print(d+1)
            elif 10*c<5:
                print(d)
        elif c<10:
            if 10*c>=15:
                print(d+1)
            elif 10*c<15:
                print(d)
        elif c>=10:
            k=c//10
            if 10*c>=10*k+5:
                print(d+1)
            elif 10*c<10*k+5:
                print(d)