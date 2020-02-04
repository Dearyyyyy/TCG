# coding=utf-8
a=int(input())
b=int(input())
c=int(input())
if a+b<=c or b+c<=a or a+c<=b:
    print("ERROR")
elif a==b and b==c:
    print("DB")
elif a==b or b==c or a==c:
    print("DY")
elif a*a+b*b==c*c:
    print("ZJ")
else:
    print("PT")