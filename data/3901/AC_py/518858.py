# coding=utf-8
N=int(input())
a,b=1,0
def Taozi(sheng):
    sheng=(sheng+1)*2
    return sheng
for i in range(N-1):
        b=Taozi(a)
        a=b
print(a)