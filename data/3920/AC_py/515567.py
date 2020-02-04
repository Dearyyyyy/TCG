# coding=utf-8
aNum = input()
a1 = int(aNum[0])
a2 = int(aNum[1])
a3 = int(aNum[2])
aNum = int(aNum)

if aNum == a1**3+a2**3+a3**3:
    print("YES")
else:
    print("NO")