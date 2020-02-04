# coding=utf-8
while True:
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    if a+b<=c and abs(a-b)<=c:
        print("ERROR")
    elif a==b and b==c:
        print("DB")
    elif a==b or b==c or c==b:
        print("ZJ")
    elif a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a:
        print("PT")