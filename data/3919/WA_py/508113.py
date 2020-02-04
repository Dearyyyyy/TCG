# coding=utf-8
while True:
    a,b,c=input().split()
    if(int(a)+int(b)>int(c) and int(a)-int(b)<int(c)):
        if(int(a)==int(b) and int(b)==int(c)):
            print("DB")
        elif(int(a)==int(b) or int(b)==int(c) or int(a)==int(c)):
            print("DY")
        elif(int(a)**2+int(b)**2==int(c)**2 or int(a)**2+int(c)**2==int(b)**2 or int(c)**2+int(b)**2==int(a)**2 ):
            print("Zj")
        else:
            print("PT")
    else:
        print("ERROR")