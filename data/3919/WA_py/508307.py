# coding=utf-8
a,b,c = input().split()
d,e,f = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
while True:
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
while True:
  if d+e<=f or f+e<=d or d+f<=e:
    print('ERROR')
    break
  elif d == e == f:
    print ('DB')
    break
  elif d == e or d==f or e==f:
    print ('DY')
    break
  elif d*d == e*e + f*f or e*e == d*d+ f*f or f*f== d*d + e*e:
    print ('ZJ')
    break
  else:
    print ('PT')
    break