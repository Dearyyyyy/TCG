# coding=utf-8
while True:
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    if a+b>c and a+c>b and c+b>a:
       if a==b!=c or a==c!=b or b==c!=a:
          print("DY")
       elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
          print("ZJ")
       elif a==b==c:
          print("DB")
       else:
          print("PT")
    else:
       print("ERROR")