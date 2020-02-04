# coding=utf-8
while True :
  n=input()
  H=0
  M=0
  str1=''
  str2=''
  str3=''
  l=''
  k=0
  cha=0
  for i in range(int(n)):
    t,a,b=input().split()
    #print(str1,'+/*')
    if b=='AC' and str1.find(a)==-1:
        str1=str1+a
        k=str2.count(a)
        h=int(t[0:2])-18
        m=int(t[3:5])+k*20
        h=h+H
        m=m+M
        H,M=h,m
       # print(h,m,'***')
        if m>=60:
            h=h+int(m/60)
            m=m-int(m/60)*60
        if m<0:
          h=h-int(m/60)-1
          m=m+int(m/60)*60+60
        h,m=str(h),str(m)
        if len(h)==1:
            h='0'+h
        if len(m)==1:
            m='0'+m
        str3=h+':'+m
        h,m=int(h),int(m)        
    elif b!='AC':
        str2=str2+a
       # print(len(str2))
  print(str3)