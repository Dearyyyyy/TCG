# coding=utf-8
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
while True:
    if a+b<=c or a+c<=b or c+b<=a:
        print("ERROR")
    elif a*a==b*b and b*b==c*c:
        print("DB")
    elif a*a==b*b or a*a==c*c or c*c==b*b:
        print("DY")
    elif a*a+b*b==c*c or c*c+b*b==a*a or a*a+c*c==b*b:
        print("ZJ")
    else:
        print("PT")
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)