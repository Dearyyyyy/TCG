# coding=utf-8
while True:
 import math
 a,b=input().split()
 a,b=int(a),int(b)
 if b==0:
    print('error')
 else:
    c=a/b
    d=round(c)+0.5
    print(int(d))