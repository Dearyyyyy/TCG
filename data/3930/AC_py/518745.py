# coding=utf-8
x=input()
x=int(x)
for i in range(0,x):
            n=input()
            n=int(n)
            L=[]
            a=n//100
            n=n-a*100
            L.append(a)
            a=n//50
            n=n-a*50
            L.append(a)
            a=n//20
            n=n-a*20
            L.append(a)
            a=n//10
            n=n-a*10
            L.append(a)
            a=n//5
            n=n-a*5
            L.append(a)
            a=n//2
            n=n-a*2
            L.append(a)
            a=n
            L.append(a)
            L=L[::-1]
            for i in L:
                print(i,end=' ')
            print("")