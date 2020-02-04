# coding=utf-8
while True:
  a,b,c = input().split()
  a = int(a)
  b = int(b)
  c = int(c)
  if a+b<=c or a+c<=b or b+c<=a:
    print('ERROR')
    break
  elif a == b == c:
    print ('DB')
    break
  elif a == b or a==c or b==c:
    print ('DY')
    break
  elif a*a == b*b + c*c or b*b == c*c+ a*a or c*c== a*a + b*b:
    print ('ZJ')
    break
  else:
    print ('PT')
    break