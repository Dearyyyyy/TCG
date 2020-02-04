# coding=utf-8
while True:
    s=input()
    if len(s)==1:
       print('YES')
    else:
        count=1
        for i in range(len(s)//2):
            if s[i]!=s[len(s)-i-1]:
                count=0
        if count==1:
            print('YES')
        else:
            print('NO')