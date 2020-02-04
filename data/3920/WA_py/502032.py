# coding=utf-8
# -*- coding: UTF-8 -*-
import string
from math import sqrt
import sys
from math import pi
from string import maketrans
from copy import deepcopy
def Shuixianhua(number):
    n1 = number/100
    n2 = (number%100)/10
    n3 = (number%100)%10
    if (pow(n1,3) + pow(n2,3) + pow(n3,3)) == number:
        return "YES"
    else:
        return "NO"
def main_run():
    num = input()
    print(Shuixianhua(num))

if __name__ == "__main__":
    main_run()