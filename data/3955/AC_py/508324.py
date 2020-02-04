# coding=utf-8
while True:
    c=""
    a,b = input().split()
    lena=len(a)
    lenb=len(b)
    if len(a)!=len(b):
        print("No")

    else :
        for i in range(len(a)):
            a = a[1:] + a[0]

            if a==b:
                print("Yes")
                break
        else:
            print("No")