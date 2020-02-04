# coding=utf-8
a = input().split()
b = input().split()
c = input().split()
a[1],b[0]=b[0],a[1]
a[2],c[0]=c[0],a[2]
b[2],c[1]=c[1],b[2]
print(a,'\n',b,'\n',c)