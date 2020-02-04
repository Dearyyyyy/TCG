# coding=utf-8
while(True):
    a,b,c = input().split()
    a = int(a); b = int(b); c = int(c)
    if a + b > c and a + c > b and b + c > a :
        if a == b == c :
            print("DB")
        elif a == b or a == c or b == c :
            print("DY")
        elif a**2 + b**2 - c**2 == 0 or a**2 + c**2 - b**2 == 0 or b**2 + c**2 - a**2 == 0 :
            print("ZJ")
        else :
            print("PT")
    else :
        print("ERROR")