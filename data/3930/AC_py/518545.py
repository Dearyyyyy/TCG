# coding=utf-8
a = (1,2,5,10,20,50,100)
n = int(input())
for i in range(n):
    r = [0 for i in range(7)]
    t = int(input())
    r[6] = int(t/100)
    r[5] = int((t%100)/50)
    r[4] = int((t%50)/20)
    r[3] = int((t%50%20)/10)
    r[2] = int((t%50%20%10)/5)
    r[1] = int((t%50%20%10%5)/2)
    r[0] = t%50%20%10%5%2
    print("%d"%r[0],"%d"%r[1],"%d"%r[2],"%d"%r[3],"%d"%r[4],"%d"%r[5],"%d"%r[6])