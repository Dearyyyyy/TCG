# coding=utf-8
n=int(input())
s=[0,0,0,0,0,0,0]
for i in range(0,n):
    m=int(input())
    s[6]=m//100
    m-=s[6]*100
    s[5]=m//50
    m-=s[5]*50
    s[4]=m//20
    m-=s[4]*20
    s[3]=m//10
    m-=s[3]*10
    s[2]=m//5
    m-=s[2]*5
    s[1]=m//2
    m-=s[1]*2
    s[0]=m
    print(*s)