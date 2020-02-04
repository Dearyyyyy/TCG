# coding=utf-8
while True:
    a,b=input().split()
    a=int(a)
    b=int(b)
   
    if b==0:
        print('error')
    
    elif a/b-a//b>=0.5:
        print(a//b+1)
    else:
        print(a//b)