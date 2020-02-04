# coding=utf-8
def tun(now,a):
    for i in range(10000):
        if a*i>now:
            return i-1
            break

if __name__ == '__main__':
    n=input()
    n=int(n)
    while True:
        a=input()
        a=int(a)

        a7=tun(a,100)
        
        a=a-100*a7
        a6=tun(a,50)
       
        a=a-50*a6
        a5=tun(a,20)
      
        a=a-20*a5
        a4=tun(a,10)
       
        a=a-10*a4
        a3=tun(a,5)
        
        a=a-5*a3
        a2=tun(a,2)
        
        a=a-2*a2
        a1=tun(a,1)
        print(a1,a2,a3,a4,a5,a6,a7)