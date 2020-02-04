# coding=utf-8
a,b,c=map(int,input().split())
if a+b<=c or a+c<=b or b+c<=a:
    print("ERROR")
elif a==b==c:
    print("DB")
elif a==b and a!=c or b==c and b!=a or a==c and a!=b:
    print("DY")
elif a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a:
    print("ZJ")
else:
    print("PT")