# coding=utf-8
n=int(input())
for i in range(n):
    a=int(input())
    b=a//100
    c=a%100//50
    d=a%100%50//20
    e=a%100%50%20//10
    f=a%100%50%20%10//5
    g=a%100%50%20%10%5//2
    i=a%100%50%20%10%5%2//1
    print(i,g,f,e,d,c,b,end=" ")
    print("\n",end="")