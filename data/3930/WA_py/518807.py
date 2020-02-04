# coding=utf-8
 l=(1,2,5,10,20,50,100)
n=int(input())
for i in range(n):
    a=[0 for i in range(7)]
    b=int(input())
    a[6]=int(t/100)
    a[5]=int((t%100)/50)
    a[4]=int((t%50)/20)
    a[3]=int((t%50%20)/10)
    a[2]=int((t%50%20%10)/5)
    a[1]=int(((t%50%20%10)%5)/2)
    r[0]=t%50%20%10%5%2
    print("%d"%r[0],"%d"%r[1],"%d"%r[2],"%d"%r[3],"%d"%r[4],"%d"%r[5],"%d"%r[6])