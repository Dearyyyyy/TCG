# coding=utf-8
while True:
    n=int(input())
    str=[0 for _ in range(26)]
    count=[0 for _ in range(26)]
    for _ in range(n):
        time,c,s=input().split()
        a,b=time.split(':')
        a=int(a);b=int(b)

        if(str[ord(c)-ord('A')]==0):
            if s=='AC':
                str[ord(c)-ord('A')]=1
                count[ord(c)-ord('A')]+= (a-18)*60+b
            else:count[ord(c)-ord('A')]+=20
    p=0
    i=0
    while i<26:
        if str[i]:
            p+=count[i]
        i +=1
    q=p/60
    print("%02d:%02d" % (int(q), int(p%60)))