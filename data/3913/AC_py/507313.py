# coding=utf-8
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
c=[int(i) for i in input().split()]
r=[a,b,c]
r=[[row[i] for row in r] for i in range(len(r[0]))]
for i in r:
    print(i[0],i[1],i[2])