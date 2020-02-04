# coding=utf-8
while True:
    a,b = input().split()
    if(b==0):
        print("error")
    else:
        c = int(a)/int(b)
        print(round(c))