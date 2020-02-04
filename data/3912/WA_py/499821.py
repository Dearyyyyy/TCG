a = map(lambda x:float(x), raw_input().split())

#b = a[1]
#c = a[2]
a = a[0]
c = 'prime'
for i in range(2,int(a**0.5 +1)):
    if a%i==0:
        c = 'not prime'
        break
print c