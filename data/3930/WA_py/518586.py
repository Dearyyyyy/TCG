# coding=utf-8
c = [100,50,20,10,5,2,1]
num = int(input())
for i in range(0,num):
    c1 = []
    n = int(input())
    for j in c:
        c1.append(n//j)
        n = n%j 
    s = ""
    for k in c1:
        s1 = str(k)+" "+s1
    print(s1)