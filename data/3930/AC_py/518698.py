# coding=utf-8
n=int(input())
for i in range(n+1):
    m=int(input())
    a=m//100
    b=(m-a*100)//50
    c=(m-a*100-b*50)//20
    d=(m-a*100-b*50-c*20)//10
    e=(m-a*100-b*50-c*20-d*10)//5
    f=(m-a*100-b*50-c*20-d*10-e*5)//2
    g=m-a*100-b*50-c*20-d*10-e*5-f*2
    print("%d %d %d %d %d %d %d"%(g,f,e,d,c,b,a))