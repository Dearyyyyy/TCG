# coding=utf-8
while True:
   a=int(input())
   count=[0 for i in range(26)]
   str=[0 for i in range (26)]
   for i in range(a):
    time,p,q=input().split()
    x,y=time.split(":")
    x=int(x)
    y=int(y)
    if(str[ord(p)-ord("A")]==0):
       if q=="AC":
           str[ord(p)-ord("A")]=1
           count[ord(p)-ord("A")]+=(x-18)*60+y
       else:
          count[ord(p)-ord("A")]+=20
   k=0
   h=0
   while k<26:
           if str[k]:
            h+=count[k]
           k=k+1
   print("%02d:%02d"%(int(h/60),int(h%60)))