# coding=utf-8
n=int(input())
i=1
while i<n:
    a=int(input())
    b=int(a/100)
    c=int((a-b*100)/50)
    d=int((a-b*100-c*50)/20)
    e=int((a-b*100-c*50-d*20)/10)
    f=int((a-b*100-c*50-d*20-e*10)/5)
    g=int((a-b*100-c*50-d*20-e*10-f*5)/2)
    h=int((a-b*100-c*50-d*20-e*10-f*5-g*2)/1)
    print(h, g, f, e, d, c, b,)
    i+1