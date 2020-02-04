# coding=utf-8
while 1:
    n=input()
    n=int(n)
    title=""
    count=[]
    hour=[]
    minute=[]
    AC=[]
    for i in range(n):
        time,title1,status=input().split()
        if title1 in title:
            count[title.find(title1)]+=1
        else:
            count.append(0)
            title=title+title1
        if status=='AC'and title not in AC:
           h=int(time[:2])-18
           m=int(time[3:])
           hour.append(h)
           minute.append(m+20*count[title.find(title1)])
           AC.append(title1)
    sum1=0
    for i in minute:
        sum1+=i
    sum2=0
    for j in hour:
        sum2+=j
    sum2,sum1=sum2+int(sum1/60),sum1%60
    print("{:02d}:{:02d}".format(sum2,sum1))