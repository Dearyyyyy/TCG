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
        else:
            if 10*c>=10*d+5:
                print(d+1)
            elif 10*c<10*d+5:
                print(d)