# coding=utf-8
n=input()
n=int(n)
i=1
while i<=n:
   a=input()
   a=int(a)
   b=a//100
   c=(a-b*100)//50
   d=(a-b*100-c*50)//20
   e=(a-b*100-c*50-d*20)//10
   f=(a-b*100-c*50-d*20-e*10)//5
   g=(a-b*100-c*50-d*20-e*10-f*5)//2
   h=(a-b*100-c*50-d*20-e*10-f*5-g*2)//1
   print(h,g,f,e,d,c,b)