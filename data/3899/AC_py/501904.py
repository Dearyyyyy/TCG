# coding=utf-8
n=int(input())
i=2
j=1
sum=0
for t in range(0,n):
    sum += i/j
    k=j 
    j=i 
    i=i+k 
print(round(sum,2))