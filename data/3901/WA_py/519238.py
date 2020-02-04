# coding=utf-8
t=int(input())
def judge(j):
    x=j
    if j=='6':
        x='9'
    elif j=='9':
        x='6'
    return x
a=[None]*t
m=[x for x in input().split()]
for i in range(0,t):
    L=[]
    for j in m[i]:
        j=judge(j)
        L.append(j)
    L=L[::-1]
    a[i]='0'
    for k in L:
        a[i]+=k
    a[i]=int(a[i])
      
      
if a[0]<a[1]:
    d=a[t-1]+1
else:
    d=a[t-1]-1
      
      
d=str(d)
L=[]
for j in d:
    j=judge(j)
    L.append(j)
L=L[::-1]
e='0'
for k in L:
    e+=k
e=e[1:]
print(e)