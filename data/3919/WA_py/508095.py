# coding=utf-8
while True:
    a,b,c=map(int,input().split())
    if(a+b>c and a+c>b and b+c>a):
        if(a==b or b==c or a==c):
            print("dy")
        elif(a==b==c):
            print("db")
        elif(a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a):
            print("zj")
        else:
            print("pt")
    else:
        print("ERROR")