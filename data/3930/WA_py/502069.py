n = input()

a = [map(lambda x:int(x), raw_input().split()) for x in range(n)]

#a = [[189]]

for num in a:
    num = num[0]
    m = [1, 2, 5, 10, 20, 50, 100][::-1]
    strr = ''
    for i in m:
        strr = str(num / i)+' ' + strr
        num = num % i

    print strr