# coding=utf-8
a = input().split()
b = input().split()
c = input().split()
a[1],b[0]=int(b[0]),int(a[1])
a[2],c[0]=int(c[0]),int(a[2])
b[2],c[1]=int(c[1]),int(b[2])
a[0],b[1],c[2] = int(a[0]),int(b[1]),int(c[2])
print(a,b,c)