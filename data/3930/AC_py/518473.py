# coding=utf-8
n=int(input())
for i in range(n):
    a=int(input())
    b=a//100
    b1=a%100
    c=b1//50
    c1=b1%50
    d=c1//20
    d1=c1%20
    e=d1//10
    e1=d1%10
    f=e1//5
    f1=e1%5
    g=f1//2
    g1=f1%2
    h=g1//1
    h1=g1%1
    print(h,g,f,e,d,c,b)