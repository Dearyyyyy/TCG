# coding=utf-8
r1 = input().split()
r2 = input().split()
r3 = input().split()
r1 = [int(i) for i in r1]
r2 = [int(i) for i in r2]
r3 = [int(i) for i in r3]
r = [r1,r2,r3]
r = [[row[i] for row in r] for i in range(len(r[0]))]
for i in r:
    print(i[0],i[1],i[2])