# coding=utf-8
a,b=input().split()

while a!="":
    if int(b)==0:
        print("error")
    else:
        c=int(a)//int(b)
        if int(a)%int(b)*2>=int(b):
           c=c+1
        print(c)
    a,b=input().split()