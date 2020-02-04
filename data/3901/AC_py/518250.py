# coding=utf-8
def main():
    n=int(input())
    q=1
    for i in range(n-1):
        q=(q+1)*2
    return q
c=main()
print(c)