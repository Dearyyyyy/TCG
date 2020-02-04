# coding=utf-8
 l=(1,2,5,10,20,50,100)
n=int(input())
for i in range(n):
    a=[0 for i in range(7)]
    t=int(input())
    a[6]=int(t/100)
    a[5]=int((t%100)/50)
    a[4]=int((t%50)/20)
    a[3]=int((t%50%20)/10)
    a[2]=int((t%50%20%10)/5)
    a[1]=int(((t%50%20%10)%5)/2)
    a[0]=t%50%20%10%5%2
    print("%d"%a[0],"%d"%a[1],"%d"%a[2],"%d"%a[3],"%d"%a[4],"%d"%a[5],"%d"%a[6])