m = 0
for n in range(1, 1855663):
  b = bin(n)[2:]
  if(n%5==0):
    b+='101'
  else:
    b+='1'
  r=int(b, 2)
  if(r%7==0):
    b+='111'
  else:
    b+='1'
  r = int(b, 2)
  if(r<1855663):
    m=n
print(m)