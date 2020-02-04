# coding=utf-8
a=input()
h=int(a)
a=list(a)
b=int(a[0])
c=int(a[1])
d=int(a[2])
if h==b*b*b+c*c*c+d*d*d :
    print("YES")
else:
    print("NO")