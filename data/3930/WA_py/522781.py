# coding=utf-8
def tun(now,a):
    for i in range(100):
        if a*i>=now:
            return i-1
            break

if __name__ == '__main__':
    n=input()
    n=int(n)
    while True:
        a=input()
        a=int(a)

        a7=tun(a,100)
        print("%d " % a7,end="")

        a=a-100*a7
        a6=tun(a,50)
        print("%d " % a6,end="")

        a=a-50*a6
        a5=tun(a,20)
        print("%d " % a5,end="")

        a=a-20*a5
        a4=tun(a,10)
        print("%d " % a4,end="")

        a=a-10*a4
        a3=tun(a,5)
        print("%d " % a3,end="")