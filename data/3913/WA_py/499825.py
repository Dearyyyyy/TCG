a = [map(lambda x:int(x), raw_input().split()) for x in range(3)]

#b = a[1]
#c = a[2]
#a = a[0]
for j in range(3):
    for i in range (3):
        print(a[i][j])
    print('')