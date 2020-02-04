# coding=utf-8
n=int(input())
for i in range(1,n+1):
    a=int(input())
    s=a//100
    q=a%100//50
    r=a%100%50//20
    t=a%100%50%20//10
    u=a%100%50%20%10//5
    v=a%100%50%20%10%5//2
    w=a%100%50%20%10%5%2
    print('%d %d %d %d %d %d %d'%(w,v,u,t,r,q,s,))