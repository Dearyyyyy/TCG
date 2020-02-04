# coding=utf-8
def main():
    n=int(input())
    a=n//100
    b=(n%100)//10
    c=n%10
    if (n==a*a*a+b*b*b+c*c*c):
        print("YES")
    else:
        print("NO")
main()