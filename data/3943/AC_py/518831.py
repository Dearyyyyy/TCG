# coding=utf-8

aList = [0] * 10

def func(i : int, n : int):
    if i == n:
        for j in aList:
            print(j, end=" ")
        print("")
        return
    for k in range(1,n+1):
        isShow = False
        for j in range(i):
            if aList[j] == k:
                isShow = True
        if not isShow:
            aList[i] = k
            func(i+1,n)

if __name__=="__main__":
    while True:
        n = input()
        n = int(n)
        if n == 0:
            break;
        aList = [0] * n
        func(0,n)