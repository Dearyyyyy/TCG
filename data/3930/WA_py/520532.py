# coding=utf-8
def fun():
    x=[]
    n=int(input())
    d = {"1":0,"2":0,"5":0,"10":0,"20":0,"50":0,"100":0}
    while(n):
        if n>=100:
            d["100"]=int(n/100)
            n=n%100
        elif 50<=n<100:
            d["50"]=int(n/50)
            n=n%50
        elif 20<=n<50:
            d["20"]=int(n/20)
            n=n%20
        elif 10<=n<20:
            d["10"]=int(n/10)
            n=n%10
        elif 5<=n<10:
            d["5"]=int(n/5)
            n=n%5
        elif 2<=n<5:
            d["2"]=int(n/2)
            n=n%2
        elif n==1:
            d["1"]=1
            n=0
    for j in d:
        x.append(d[j])
        # print(d[j],end=" ")
    for i in x:
        print(i,end=" ")
x=int(input())
for i in range(x):
    fun()
    print()