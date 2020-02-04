# coding=utf-8
while True :
    a,b=input().split()
    if int(b)==0:
        print('error')
    else :
        c=int(a)/int(b)
        if int(a)-int(b)*int(c)>=(float(b)/2):
            c+=1
        print(int(c))