# coding=utf-8
while True:
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if a + b > c and a + c > b and c + b > a:
        if a == b and b == c:
            print("DB")
        elif a == b or b == c:
            print("DY")
        elif a * a == b * b + c * c or b * b == a * a + c * c or c * c == b * b + a * a:
            print("ZJ")
        else:
            print("PT")
    else:
        print("ERROR")