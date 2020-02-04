# coding=utf-8
while True:
    a,b,c = map(int,input().split())
    if a+b<=c or b+c<=a or a+c<=b:
        print("ERROR")
    elif a==b and b==c:
        print("DB")
    elif a==b and b!=c or b==c and c!=a or a==c and c!=b:
        print("DY")
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print("ZJ")
    else:
        print("PT")