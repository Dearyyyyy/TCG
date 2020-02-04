# coding=utf-8
n=int(input())
sm=0
a=2
b=1
for i in range(n):
    sm=a/b+sm
    a,b=a+b,a
print("%.2f"%sm)