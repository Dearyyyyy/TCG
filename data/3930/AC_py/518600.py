# coding=utf-8
s = [0,0,0,0,0,0,0]
res=""
n=int(input())
for i in range(n):
    k = int(input())
    s[6] = k//100
    k = k - (s[6]*100)
    s[5] = k//50
    k = k - (s[5] * 50)
    s[4] = k//20
    k = k - (s[4] * 20)
    s[3] = k//10
    k = k - (s[3] * 10)
    s[2] = k//5
    k = k - (s[2] * 5)
    s[1] = k//2
    k = k - (s[1] * 2)
    s[0] = k//1
    for j in s:
        print(j)