# coding=utf-8
a,b,c=input().split()
d,e,f=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
f=int(f)
if a+b>c and a+c>b and c+b>a:
    if a==b or a==c or b==c:
       print("DY")
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
       print("ZJ")
    elif a==b==c:
       print("DB")
    else:
        print("PT")
else:
    print("ERROR")
while True:
    if d+e>f and d+f>e and e+f>d:
        if d==e or d==f or e==f:
           print("DY")
        elif d*d+e*e==f*f or d*d+f*f==e*e or f*f+e*e==d*d:
           print("ZJ")
        elif d==e==f:
           print("DB")
        else:
            print("PT")
    else:
        print("ERROR")
    break