# coding=utf-8
from math import *


def F(x: int, n: int) -> float:
    if x == 0:
        return sin(n)
    else:
        return sin(F(x - 1, n))


nums = [1]


def ran(n: int, ls: list, ls2: list):
    lst = ls
    if n == len(ls):
        for i in ls2:
            print(i, end=' ')
        print()
        return

    for i in range(len(lst)):
        if lst[i] == 1:
            lst[i] = 0
            ls2.append(i+1)
            ran(n+1, lst, ls2)
            ls2.pop()
            lst[i] = 1
    return


def main():
    # while True:
    # n = eval(input())
    # print(cnt(n))
    while True:
        n = eval(input())
        lst = [1] * n
        for i in range(len(lst)):
            if lst[i] == 1:
                lst[i] = 0
                lst2 = []
                lst2.append(i+1)
                ran(1, lst, lst2)
                lst2.pop()
                lst[i] = 1


main()