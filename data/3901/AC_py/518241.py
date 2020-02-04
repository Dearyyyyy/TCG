# coding=utf-8
def eat(n:int,cnt : int)->int:
    if n==cnt:
        return 1
    else:
        return (eat(n,cnt+1)+1)*2

def main():
    n = eval(input())
    print(eat(n,1))

main()