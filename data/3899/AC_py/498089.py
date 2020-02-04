# coding=utf-8
n=int(input())
s1=[]
s2=[]
i=1
j=0
k=1
s=0
while(k<=n+2):
    s1.append(i)
    i=i+j
    j=i-j
    k=k+1
i=1
j=0
k=1
s=0
while(k<=n+1):
    s2.append(i)
    i=i+j
    j=i-j
    k=k+1
s1.remove(1)
s1.remove(1)
s2.remove(1)
for i in range(n):
    s=s+s1[i]/s2[i]
print('%.2f'%s)