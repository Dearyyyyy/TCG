# coding=utf-8
while True:
 stra=input()
 a0=stra.count('1Y')
 a1=stra.count('1N')
 a2=stra.count('2Y')
 a3=stra.count('2N')
 a4=stra.count('3Y')
 a5=stra.count('3N')
 a6=stra.count('R')
 a7=stra.count('A')
 a8=stra.count('S')
 a9=stra.count('B')
 a10=stra.count('T')
 su=(1*a0+2*a2+3*a4+a6+a7+a8+a9)-(a3+a5)-a1-a10
 print(su)