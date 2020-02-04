# coding=utf-8
n=int(input())
num=0
x1=1
y1=2
x2=2
y2=3
num=(y1/x1)+(y2/x2)
for i in range(n-2):
    x=x1+x2
    y=y1+y2
    num+=y/x
    y1=y2
    x1=x2
    y2=y
    x2=x
print("%.2f"%num)