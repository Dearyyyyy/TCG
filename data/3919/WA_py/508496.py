# coding=utf-8
a,b,c=input().split()
d,e,f=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
f=int(f)
if a+b>c and b+c>a and a+c>b:
    if a==b==c:
        g="DB"
    elif a==b or b==c or c==a:
        g="DY"
    elif a**2+b**2==c**2 or b**2+c**2==a**2 or a**2+c**2==b**2:
        g="ZJ"
    else:
        g="PT"
else:
    g="ERROR"
if d+e>f and e+f>d and d+f>e:
    if d==e==f:
        h="DB"
    elif d==e or e==f or f==d:
        h="DY"
    elif d**2+e**2==f**2 or e**2+f**2==d**2 or d**2+f**2==e**2:
        h="ZJ"
    else:
        h="PT"
else:
    h="ERROR"
print(g)
print(h)