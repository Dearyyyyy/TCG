# coding=utf-8
while True:
    a,b,c=map(int, input().split())
    if a==b and b==c:
        print("DB")
    elif a==b or a==c or b==c:
        print("DY")
    elif a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
        print("ZJ")
    elif a+b>c:
        print("PT")
    elif a+b<=c:
        print("ERROR")