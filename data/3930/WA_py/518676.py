# coding=utf-8
while True:
    s1=[]
    n=input()
    n=int(n)
    a=n//100
    print(a)
    s1.append(a)
    b=(n-a*100)//50
    s1.append(b)
    c=(n-a*100-b*50)//20
    s1.append(c)
    d=(n-a*100-b*50-c*20)//10
    s1.append(d)
    e=(n-a*100-b*50-c*20-d*10)//5
    s1.append(e)
    f=(n-a*100-b*50-c*20-d*10-e*5)//2
    s1.append(f)
    g=n-a*100-b*50-c*20-d*10-e*5-f*2
    s1.append(g)
    s1.reverse()
    for i in s1:
        print(i,end=' ')