# coding=utf-8
while True:
    a,b=input().split()
    a,b=int(a),int(b)
    if(b==0):
        print('error')

    else:
        c=a/b
        d=(c+0.5)/1
        print(int(d))