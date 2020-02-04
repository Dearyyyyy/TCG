# coding=utf-8
while 1:
    x,y,z=map(int,input().split())
    if(x+y>z and x+z>y and y+z>x):
        if(x==y==z):
            print("DB")
        elif(x==y or x==z or y==z):
            print("DY")
        elif(x*x+y*y==z*z or x*x+z*z==y*y or y*y+z*z==x*x):
            print("ZJ")
        else:
            print("PT")
    else:
        print("ERROR")