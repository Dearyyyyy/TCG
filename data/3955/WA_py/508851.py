# coding=utf-8
def equal(str1, str2):
    h = [0] * 26
    for ch in str1:
        h[ord(ch)-ord('a')] += 1
    for ch in str2:
        h[ord(ch)-ord('a')] -= 1
    for elem in h:
        if elem != 0:
            return False
    return True
while True:
    a,b=map(str,input().split())
    if equal(a,b)==True:
        print("Yes")
    else:
        print("No")