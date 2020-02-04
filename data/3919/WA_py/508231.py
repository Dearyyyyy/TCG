# coding=utf-8
while True:
 a,b,c=input().split()
 a,b,c=int(a),int(b),int(c)
 if (a+b>c)or(a-b<c):
     if (a==b)and(b==c):
        print('DB') 
     elif (a==b)or(a==c)or(b==c):
        print('DY')
     elif (a**2+b**2==c**2) or (b**2+c**2==a**2) or (a**2+c**2==b**2):
        print('ZJ')
     else:
        print('PT')
 else:
    print('ERROR')