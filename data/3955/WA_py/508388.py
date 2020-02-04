# coding=utf-8
def pd(a):


        Len = len(a)
        count = 0
        flag = 1
        while count < Len // 2:
            if a[count] != a[Len - count - 1]:
                flag = 0
                break
            count += 1
        if flag == 1:
            return 1
        else:
            return 0

a,b=input().split()
c=a+b
if(pd(c)):
    print('YES')
else:
    print('NO')