# coding=utf-8
a=input().split()
b=input().split()
a=[int(i) for i in a]
b=[int(i) for i in b]
if a[0]+a[1]<=a[2] or a[0]+a[2]<=a[1] or a[1]+a[2]<=a[0]:
    print("ERROR")
elif a[0]==a[1]==a[2]:
    print("DB")
elif a[0]==a[1]!=a[2] or a[0]==a[2]!=a[1] or a[1]==a[2]!=a[0]:
    print("DY")
elif a[0]*a[0]+a[1]*a[1]==a[2]*a[2] or a[0]*a[0]+a[2]*a[2]==a[1]*a[1] or  a[2]*a[2]+a[1]*a[1]==a[0]*a[0]:
    print("ZJ")
else:
    print("PT")
if b[0]+b[1]<b[2] or b[0]+b[2]<b[1] or b[1]+b[2]<b[0]:
    print("ERROR")
elif b[0]==b[1]==b[2]:
    print("DB")
elif b[0]==b[1]!=b[2] or b[0]==b[2]!=b[1] or b[1]==b[2]!=b[0]:
    print("DY")
elif b[0]*b[0]+b[1]*b[1]==b[2]*b[2] or b[0]*b[0]+b[2]*b[2]==b[1]*b[1] or  b[2]*b[2]+b[1]*b[1]==b[0]*b[0]:
    print("ZJ")
else:
    print("PT")