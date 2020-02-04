# coding=utf-8
while True:
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    if a+b>c and b+c>a and a+c>b :
        if a==b and b==c and a==c:
            print("DB")
        elif a==b or b==c or a==c:
            print("DY")
        elif a**2+b**2==c**2 or c**2+b**2==a**2 or c**2+a**2==b**2:
            print("ZJ")
        else:
            print("PT")
    else:
        print("ERROR")