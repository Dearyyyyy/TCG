# coding=utf-8
a=int(input())
for i in range(0,a):
    t=int(input())
    s1=t//100
    t=t-s1*100
    s2=t//50
    t=t-s2*50
    s3=t//20
    t=t-s3*20
    s4=t//10
    t=t-s4*10
    s5=t//5
    t=t-s5*5
    s6=t//2
    t=t-s6*2
    s7=t//1
    print("%d %d %d %d %d %d %d" %(s7,s6,s5,s4,s3,s2,s1))