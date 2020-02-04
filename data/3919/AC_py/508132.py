# coding=utf-8
while True:
    n=input().split()
    a=int(n[0])
    b=int(n[1])
    c=int(n[2])
    if (a+b)<=c or (a+c)<=b or (b+c)<=a:
        print("ERROR")
    elif a==b and b==c :
        print("DB")
    elif a==b or a==c or b==c:
        print("DY")
    elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("ZJ")
    else :
        print("PT")