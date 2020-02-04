# coding=utf-8
while True:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if b==0:
        print("error")
    elif 2*(a%b)>=b:
        c=int(a/b)+1
        print(c)
    else:
        c=int(a/b)
        print(c)