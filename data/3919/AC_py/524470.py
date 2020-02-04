# coding=utf-8
s = input().split()
while s:
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    if a+b>c and a+c>b and b+c>a:
        if a==b and b==c:
            print("DB")
        elif a==b or b==c or a==c:
            print("DY")
        elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
            print("ZJ")
        else :
            print("PT")
    else:
        print("ERROR")
    s = input().split()