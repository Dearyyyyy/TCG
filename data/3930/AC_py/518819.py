# coding=utf-8
n=int(input())
for i in range(n):
    s=int(input())
    x1=0
    x2=0
    x5=0
    x10=0
    x20=0
    x50=0
    x100=0
    x100=s//100
    x50=(s-(x100*100))//50
    x20=(s-(x100*100)-(x50*50))//20
    x10=(s-(x100*100)-(x50*50)-(x20*20))//10
    x5=(s-(x100*100)-(x50*50)-(x20*20)-(x10*10))//5
    x2=(s-(x100*100)-(x50*50)-(x20*20)-(x10*10)-(x5*5))//2
    x1=s-(x100*100)-(x50*50)-(x20*20)-(x10*10)-(x5*5)-(x2*2)
    print("%d %d %d %d %d %d %d"%(x1,x2,x5,x10,x20,x50,x100))