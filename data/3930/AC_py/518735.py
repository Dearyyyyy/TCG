# coding=utf-8
n=int(input())
for i in range(n):
    m=int(input())
    g=m//100
    f=m%100//50
    e=m%100%50//20
    d=m%100%50%20//10
    c=m%100%50%20%10//5
    b=m%100%50%20%10%5//2
    a=m%100%50%20%10%5%2
    print("%d %d %d %d %d %d %d"%(a,b,c,d,e,f,g))