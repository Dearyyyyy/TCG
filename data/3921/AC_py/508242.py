# coding=utf-8
a=input()
a=int(a)
i=0
i=int(i)
while i<a:
    str=input()
    length=len(str)
    left=0
    right=length-1
    while left<=right:
        if str[left]==str[right]:
            left+=1
            right-=1
        else:
            break;
    if left>right:
        print("YES")
    else :
        print("NO")