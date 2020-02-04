# coding=utf-8
m=int(input())
while True:
 n=int(input())
 a=0
 b=0
 c=0
 d=0
 e=0
 f=0
 g=0

 a=n//100
 n=n%100
 b=n//50
 n=n%50
 c=n//20
 n=n%20
 d=n//10
 n=n%10
 e=n//5
 n=n%5
 f=n//2
 n=n%2
 g=n//1
 print(g,end=" ")
 print(f,end=" ")
 print(e,end=" ")
 print(d,end=" ")
 print(c,end=" ")
 print(b,end=" ")
 print(a)