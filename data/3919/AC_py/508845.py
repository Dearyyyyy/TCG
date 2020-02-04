# coding=utf-8
while True:
    a,b,c=map(int,input().split())
    if a+b<c or a+c<b or b+c<a:
        print("ERROR")
        continue
    if a==b and b==c:
        print("DB")
    elif a==b or b==c or a==c:
        print("DY")
    elif a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
        print("ZJ")
    else:
        print("PT")