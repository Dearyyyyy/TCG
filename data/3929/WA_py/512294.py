# coding=utf-8
while True :
  n=input()
  h=18
  m=0
  str1=''
  str2=''
  str3=''
  l=''
  for i in range(int(n)):
    t,a,b=input().split()
    #print(t,a,b,'+')
    if b=='AC' and str1.find(a)==-1 :
        str1=str1+a
    elif b=='AC'and str1.find(a):
        i=int(str1.find(a))
        print(str3[5*i:5*i+5])
    if b!='AC':
        str2=str2+a
       # print(int(str2.count(a)))
    if b=='AC':
        h=int(t[0:2])-h
        k=int(str2.count(a))
        m=int(t[3:5])-m+k*20
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
        print(l)