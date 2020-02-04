# coding=utf-8
import math
n=int(input())
for i in range(1,n+1):
    m=int(input())
    a=m//100
    b=(m-a*100)//50
    c=(m-a*100-b*50)//20
    d=(m-a*100-b*50-c*20)//10
    g=(m-a*100-b*50-c*20-d*10)//5
    e=(m-a*100-b*50-c*20-d*10-g*5)//2
    f=(m-a*100-b*50-c*20-d*10-g*5-e*2)//1
        
    print("%d %d %d %d %d %d %d" % (f,e,g,d,c,b,a))