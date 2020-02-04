# coding=utf-8
k=0
while True:
    s1,s2=input().split()
    for i in range(len(s1)):
       for i in range(1,len(s1)):
           if s1[i:]==s2[0:(len(s1)-i)] and s1[0:1]==s2[(len(s1)-1):]:
                k=1
    if k==1:
        print("Yse")
    else:
        print("No")