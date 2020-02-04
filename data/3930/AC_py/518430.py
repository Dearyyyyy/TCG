# coding=utf-8
from math import*
def F(x:int,n:int)->float:
    if x == 0:
        return sin(n)
    else:
        return sin(F(x-1,n))
def calMoney(n : int):
    lst = [1,2,5,10,20,50,100]
    lst1=[0]*7
    mon = n
    for i in range(6,-1,-1):
        lst1[i] = mon//lst[i]
        mon = mon % lst[i]
    for i in lst1:
        print(i,end = ' ')
    print()
def main():
  n = eval(input())
  for i in range(n):
      e = eval(input())
      calMoney(e)

main()