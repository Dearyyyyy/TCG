# coding=utf-8
def permutation(n,a,cur):
    if cur == n:
        for i in range(n): print(a[i]+1,end=' ')
        print()
    else:
        for i in range(n):
            ok = 1
            for j in range(cur):
                if a[j] == i: ok = 0
            if ok:
                a[cur] = i
                permutation(n,a,cur+1)

while True:
    n = int(input())
    a = [0 for _ in range(1000)]
    permutation(n,a,0)