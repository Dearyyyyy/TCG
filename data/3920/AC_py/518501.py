# coding=utf-8
a=input()
n,m=0,0
l=len(a)
for i in range(0,l):
    n=n+(ord(a[i])-48)*10**(l-i-1)
for i in range(0,l):
    m=m+(ord(a[i])-48)**3
if n==m:
    print('YES')
else:
    print('NO')