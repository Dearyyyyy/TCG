# coding=utf-8
r1=[int(i) for i in input().spllit()]
r2=[int(i) for i in input().spllit()]
r3=[int(i) for i in input().spllit()]
r=[r1,r2,r3]
r=[row[i] for row in r] for i in range(len(r[0]))]
for i in r:
    print(i[0],i[1],i[2])