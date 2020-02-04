# coding=utf-8
while True:
    s1,s2=input().split()
    s3=''
    for i in range(len(s1)):
        s3=s1[i:]+s1[:i]
        if s3==s2:
            print("Yes")
            break
    else:
        print("No")