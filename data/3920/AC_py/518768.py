# coding=utf-8
def findda(num):
    num = int(num)
    a = num//100
    b = (num//10)%10
    c = num%10
    if num == a*a*a+b*b*b+c*c*c:
        return "YES"
    else:
        return "NO"
data = input()
out = findda(data)
print(out)