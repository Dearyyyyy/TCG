# coding=utf-8
a=input()
a=int(a)
i=0
k=0
while i<a:
    b=input()
    b=int(b)
    i=i+1
    c=b//100
    d=(b-c*100)//50
    e=(b-c*100-d*50)//20
    f=(b-c*100-d*50-e*20)//10
    g=(b-c*100-d*50-e*20-f*10)//5
    h=(b-c*100-d*50-e*20-f*10-g*5)//2
    k=b-c*100-d*50-e*20-f*10-g*5-h*2
    print("%d %d %d %d %d %d %d"%(k,h,g,f,e,d,c))