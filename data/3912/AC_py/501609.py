# coding=utf-8
def  判断质数(n):
    s=0
    for i in range(2,n+1):
        if n%i==0:
           s=s+i
    if s==n:
        flag=1
    else:
        flag=0
    return (flag)

if __name__ == '__main__':
    n=int(input())
    f=判断质数(n)
    if f==1:
        print('prime')
    else:
        print('not prime')