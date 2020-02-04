# coding=utf-8
while True:
 n=input()
 h=18
 m=0
 k=0
 am=''
 sm=[]
 for i in range(int(n)):
     time,a,b=input().split()
     if b=='AC':
         #print(a,'++',am)
         if am.find(a)!=-1:
            x=am.index(a)
            bm=str(sm[x:x+1])
            print(bm[2:7])
            continue
         else:
             am=am+a
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
         #h=list(h)
         sm.append(h)
         #print(sm,'++')
     else :
         k+=1