# coding=utf-8
n=int(input())
q=2


p=1

s=0

for i in range (0,n):
    s=s+q/p
    
    
    t=q
    q=q+p
    
    
    p=t
print("%.2f" % s)