# coding=utf-8
while True:
    a,b=input().split()
    a,b=int(a),int(b)
    if(b==0):
        print('ERROR')

    else:
        c=a/b
        c=round(c)
        print(c)