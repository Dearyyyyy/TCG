# coding=utf-8
import sys
def ss(s):
    if len(s)<2:
        return True
    if s[0]==s[-1]:
        return ss(s[1:-1])
    else:
        return False
n=int(input())
for i in range(n):
    s=[str(i) for i in input()]
    if ss(s)==True:
        print('YES')
    else:
        print('NO')