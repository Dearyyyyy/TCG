# coding=utf-8
a=input().split()
b=input().split()
c=input().split()
e=a[1]
a[1]=b[0]
b[0]=e
e=a[2]
a[2]=c[0]
c[0]=e
e=b[2]
b[2]=c[1]
c[1]=e
for i in a:
    print(i ,end=' ')
print()
for i in b:
    print(i ,end=' ')
print()
for i in c:
    print(i ,end=' ')