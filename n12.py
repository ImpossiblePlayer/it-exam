def simple(n):
  i=2
  while i*i<=n:
    if(n%i==0):
      return False # число не простое
    i+=1
  return True

answer = []
for c1 in range(50):
  for c2 in range(50):
    s = '0' + '1'*c1 + '2'*c2
    summ_start = sum([int(x) for x in s])
    if(len(s) <=40):
      continue
    while('01' in s or '02' in s):
      s = s.replace('02', '0110', 1)
      s = s.replace('01', '220', 1)
    summ = sum([int(x) for x in s])
    if(simple(summ)):
      answer.append(summ_start)
      print(summ_start)
print(min(answer))