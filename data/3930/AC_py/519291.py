# coding=utf-8
n=int(input())
for i in range(n):
    data=int(input())
    a=data%10
    a3=a//5
    a2=(a-a3*5)//2
    a1=a-a3*5-a2*2
    b=data%100//10
    b=b*10
    b3=b//50
    b2=(b-b3*50)//20
    b1=(b-b3*50-b2*20)//10
    c=data//100
    print("%d"%a1,"%d"%a2,"%d"%a3,"%d"%b1,"%d"%b2,"%d"%b3,"%d"%c)