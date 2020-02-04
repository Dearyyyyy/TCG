# coding=utf-8
n1=[int(i) for i in input().split()]
n2=[int(i) for i in input().split()]
n3=[int(i) for i in input().split()]
n=[n1,n2,n3]
n=[[row[i] for row in n] for i in range(len(n[0]))]
for i in n:
    print(i[0],i[1],i[2])