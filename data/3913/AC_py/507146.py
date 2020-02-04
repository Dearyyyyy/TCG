# coding=utf-8
a = [int(n) for n in input().split()]
b = [int(n) for n in input().split()]
c = [int(n) for n in input().split()]
array = [a,b,c]
array = [[row[i] for row in array] for i in range(len(a))]
for i in array:
    print(i[0],i[1],i[2])