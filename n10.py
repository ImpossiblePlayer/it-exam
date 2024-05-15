f = open('10.txt', encoding="utf8")
words = [w.replace('.','').replace(';','').replace(',','') for w in f.read().split()]
# print(sum(i.lower().count('час') for i in words))
s = 0
for i in words:
  x = i[1:-2].lower().count('час')
  if(x):
    print(i, x)
  s+=x
print(s)