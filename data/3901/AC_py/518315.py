# coding=utf-8
def counting(days):
    numbs = 1
    for i in range(days-1):
        numbs = 2*(numbs+1)
    return numbs
days = input()
days = int(days)
peach = counting(days)
print(peach)