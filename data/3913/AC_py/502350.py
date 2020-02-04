# coding=utf-8
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l3 = list(map(int,input().split()))
lis = [l1,l2,l3]
i = 0
j = 0
while i<3:
   j = 0
   while j<3:
      print(lis[j][i],end = " ")
      j += 1
   print("\n",end = "")
   i += 1