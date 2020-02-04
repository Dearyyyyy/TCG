# coding=utf-8

def isNum(n:str)-> int:
    sum = 0
    for i in n:
        sum += int(i)**3
    return sum == int(n)

def main():
    n = input()
    if(isNum(n)):
        print("YES")
    else:
        print("NO")
    

main()