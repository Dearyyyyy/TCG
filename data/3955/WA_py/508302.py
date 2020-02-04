# coding=utf-8
while True:
    c=""
    a,b = input().split()
    lena=len(a)
    lenb=len(b)
    if len(a)!=len(b):
        print("No")
    c = a[1:] + a[0]
    if c == b:
        print("Yes")

    else :
        for i in range(len(a)-1):
            c = c[1:] + c[0]

            if c==b:
                print("Yes")
                break
        else:
            print("No")