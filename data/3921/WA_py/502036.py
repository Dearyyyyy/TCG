def is_palindrone(n):
    return n[::-1] == n

m = int(raw_input())
while m > 0:
    if is_palindrone(raw_input()):
        print('YES')
    else:
        print('NO')
    m -= 1