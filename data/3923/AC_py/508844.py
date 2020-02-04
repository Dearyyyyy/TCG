# coding=utf-8
while True:
  cod = input()
  b = len(cod)
  sco = 0
  nos = 0
  noh = 0
  ast = 0
  reb = 0
  ste = 0
  blo = 0
  tur = 0
  eff = 0
  tir = 0
  noft = 0
  nosft = 0
  for i in range(b):
    if cod[i]=='Y':
      sco = sco + int(cod[i-1])
      if cod[i-1]=='1':
        noft = noft+1
        nosft = nosft+1
      else:
        nos = nos +1
        noh = noh +1
    elif cod[i]=='N':
      if cod[i-1] =='1':
        noft = noft+1
      else:
        nos =nos+1
    elif cod[i]=='A':
      ast = ast + 1
    elif cod[i]=='R':
      reb = reb+1
    elif cod[i]=='S':
      ste = ste+1
    elif cod[i]=='B':
      blo = blo+1
    elif cod[i]=='T':
      tur = tur+1
    elif cod[i]=='1':
      tir = tir+1
  eff = (sco+ast+reb+ste+blo)-(nos-noh)-(noft-nosft)-tur
  print(eff)