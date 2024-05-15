def simple(n):
  i=2
  while i*i<=n:
    if(n%i==0):
      return False # число не простое
    i+=1
  return True

# answer = []
# for c1 in range(50):
#   for c2 in range(50):
#     for c3 in range(50):
#       s = '0' + '1'*c1 + '2'*c2 + '3'*c3 + '0'
#       while('00' not in s):
#         s = s.replace('01', '220', 1)
#         s = s.replace('02', '1013', 1)
#         s = s.replace('03', '120', 1)
#       if(s.count('1')==13 and s.count('2')==18):
#         print(c1+c2+c3+2)

# s='0' + '1'*31 + '2'*24 + '3'*46
# while('01' in s or '02' in s or '03' in s):
#   s = s.replace('01', '30', 1)
#   s = s.replace('02', '3103', 1)
#   s = s.replace('03', '1201', 1)
# print(s.count('3'))

# for x in range(50):
#   for y in range(50):
#     for z in range(50):
#       s = '0' + '1'*x + '2'*y + '3'*z
#       while('01' in s or '02' in s or '03' in s):
#         s = s.replace('01', '30', 1)
#         s = s.replace('02', '3103', 1)
#         s = s.replace('03', '1201', 1)
#       if(s.count('1')==31 and s.count('2')==24 and s.count('3')==46):
#         print(z)

# s = '1'*128
# c=0
# while('333' in s or '11' in s):
#   if('333' in s):
#     s = s.replace('333', '1', 1)
#   else:
#     s = s.replace('11', '3', 1)
#     c+=2
# print(c)

lines = set()
for n in range(4, 1000):
  s = '4'+'9'*n
  while('44'in s or '9299'in s or '49'in s):
    if('49' in s):
      s = s.replace('49', '944', 1)
    if('44' in s):
      s = s.replace('44','2',1)
    if('9299' in s):
      s = s.replace('9299','4',1)
  lines.add(s)
print(len(lines))