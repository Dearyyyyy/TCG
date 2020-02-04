# coding=utf-8
while True :
  n=input()
  str1=''
  str2=''
  str3=''
  l=''
  for i in range(int(n)):
    t,a,b=input().split()
   # print(str1,'+/*')
    if b=='AC' and str1.find(a)==-1:
        str1=str1+a
        h=int(t[0:2])-18
        k=int(str2.count(a))
        m=int(t[3:5])-0+k*20
      #  print(h,m,'***')
        if m>=60:
            h=h+int(m/60)
            m=m-int(m/60)*60
        h,m=str(h),str(m)
        if len(h)==1:
            h='0'+h
        if len(m)==1:
            m='0'+m
        str3=str3+h+':'+m
        l=h+':'+m
        h,m=int(h),int(m)
        print(l)        
    elif b=='AC'and str1.find(a)!=-1:
        i=int(str1.find(a))
        print(str3[5*i:5*i+5],'++')
    elif b!='AC':
        str2=str2+a
       # print(int(str2.count(a)))