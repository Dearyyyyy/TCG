# coding=utf-8
def findda(num):
    num = int(num)
    a = num%100
    b = num/10%10
    c = num%10
    if num == a**3+b**3+c**3:
        return "YES"
    else:
        return "NO"
data = input()
data = int(data)
out = findda(data)
print(out)