# coding=utf-8
n = input()
n = int(n)
for i in range(n+1):
    data = input()
    data = int(data)
    a = data//100
    b = (data-a*100)//50
    c = (data-a*100-b*50)//20
    d = (data-a*100-b*50-c*20)//10
    e = (data-a*100-b*50-c*20-d*10)//5
    f = (data-a*100-b*50-c*20-d*10-5*e)//2
    g = data-a*100-b*50-c*20-d*10-5*e-2*f
    print(g,end=' ')
    print(f,end=' ')
    print(e,end=' ')
    print(d,end=' ')
    print(c,end=' ')
    print(b,end=' ')
    print(a)