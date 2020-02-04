# coding=utf-8
while True:
    try:
        a=input().strip().split()
        a[0]=int(a[0])
        a[1]=int(a[1])
        a[2]=int(a[2])
        if a[0]+a[1]>a[2] and a[1]+a[2]>a[0] and a[0]+a[2]>a[1]:
            if a[0]==a[1] or a[1]==a[2] or a[0]==a[2]:
                if a[0]==a[1]==a[2]:
                    print("DB")
                else:
                    print("DY")

            elif a[0]**2+a[1]**2==a[2]**2 or a[2]**2+a[1]**2==a[0]**2 or a[0]**2+a[2]**2==a[1]**2:
                print("ZJ")
            else:
                print("PT")
        else:
            print("ERROR")