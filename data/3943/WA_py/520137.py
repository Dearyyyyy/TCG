# coding=utf-8
def an(n):
    if n>1:
       l=[]
       b=[]
       l=an(n-1)
       for j in l: 
           d=[]
           f=[]
           
               
           for i in range(0,n):
               d=[]
               for k in j:
                    d.append(k)
               d.insert(i,n)
               a=""
               for m in d:
                   m=str(m)
                   a=a+m
               b.append(a)     
    else:
         if n==1:
             b=[str(1)]
         else:
             if n==0:
                 b=[]
    b.sort()
    return b
n=int(input())
while(n!=""):
    c=[]
    c=an(n)
    if c==[]:
        print("")
    else:
        for i in c:
            print(i)
    n=int(input())