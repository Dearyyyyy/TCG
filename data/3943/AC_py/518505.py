# coding=utf-8
def next_permutation(A):
        n = len(A)
        last = n - 1
        i = last
        while i>0 and A[i]<A[i-1]:
                i -= 1
        if i==0:
                return False
        k = i
        j = last
        while j >= i:
                if A[j]>A[i-1] and A[j]<A[k]:
                        k = j
                j -= 1
        A[k],A[i-1] = A[i-1],A[k]
        A[i:] = A[i:][::-1]
        return True
def permutation(n):
        B = []
        A = list(range(1,n+1))
        B.append(A[::])
        flag = next_permutation(A)
        B.append(A[::])
        while flag:
                flag = next_permutation(A)
                B.append(A[::])     
                                    
        return B
while True:
    a=int(input())
    AA = permutation(a)
    for i in range(len(AA)-1):
            print(*AA[i])