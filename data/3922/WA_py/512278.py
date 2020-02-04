# coding=utf-8
def divition(a, b):
    a = float(a)
    b = float(b)
    if b == 0.0:
        return 'error'
    return round(a/b + 0.01)

def main():
    for i in range(4):
        a, b = input().split(' ')
        print(divition(a, b))

if __name__ == '__main__':
    main()