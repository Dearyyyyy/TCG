# coding=utf-8
while True:
 n=input()
 h=18
 m=0
 k=0
 for i in range(int(n)):
     time,a,b=input().split()
     if b=='AC':
         h=int(time[0:2])-h
         m=int(time[3:5])-m+k*20
         #print(h,m,'***')
         h,m=int(h),int(m)
         if m<0:
             h=int(h)-int((-m)/60)-1
             m=m+60*(int((-m)/60)+1)
            # print(int(h),int(m),'+')
         elif m>=0:
             h+=int(m/60)
             m-=60*int(m/60)
            # print(h,m,'+++')
         h,m=str(h),str(m)
         if len(h)==1:
            h=str(0)+h
         if len(m)==1:
             m=str(0)+m
         h=h+str(':')+m
         print(h)
     else :
         k+=1