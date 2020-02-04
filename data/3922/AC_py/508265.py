# coding=utf-8
while True:
    a,b = input().split()
    if(int(b)==0):
        print("error")
    else:
        c = int(a)/int(b)
        d = c+0.5
        print(int(d))