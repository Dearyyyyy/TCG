# coding=utf-8
n=int(input())
for i in range(n):
    t=[0 for i in range(7)]
    t= int(input())
    t[0]=t%50%20%10%5%2
    t[1]=int((t%50%20%10%5)/2)
    t[2]=int((t%50%20%10)/5)
    t[3]=int((t%50%20)/10)
    t[4]=int((t%50)/20)
    t[5]=int((t%100)/50)
    t[6]=int(t/100)
    print('%d'%t[0],"%d"%t[1],"%d"%t[2],"%d"%t[3],"%d"%t[4],"%d"%t[5],"%d"%t[6],)