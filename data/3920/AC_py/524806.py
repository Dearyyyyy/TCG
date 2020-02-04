# coding=utf-8
a=input()
n=int(a)
bai = int(n / 100); 
shi = int(n % 100 / 10); 
ge = int(n % 10)   

if ( n == bai ** 3 + shi ** 3 + ge ** 3 ) :
    print("YES")
else :
    print("NO")