# for i in '0123456789abcdefghi':
#   sum = int(f'98{i}79641', 19) + int(f'36{i}14', 19) + int(f'73{i}4', 19)

#   if(sum%18==0):
#     print(int(i,19), sum//18)

def change_notation(n, k):
  chars = '0123456789abcd'
  r = ""
  while(n>0):
    r += f'{chars[n%k]} '
    n//=k
  return r[::-1]

# s = 4*625**1920 + 4*125**1930 - 4*25**1940 - 3*5**1950 - 1960
# k = change_notation(s, 5)
# print(k.count('0'))

# answer = []
# for x in range(37):
#   for y in range(37):
#     a = 1*37**7 + 2*37**6 + x*37**5 + 6*37**4 + 4*37**3 + 3*37**2 + y*37 + 7
#     if(a%36==0):
#       answer.append(37*y + x)
# print(max(answer))

# for x in '0123456789abcdefghi':
#   a = int('78' + x + '79643', 19)
#   b = int('25' + x + '43', 19)
#   c = int('63' + x + '5', 19)
#   if (a + b + c) % 18 == 0:
#     print((a + b + c) // 18)

s = 625**90 + 125**120 - 5*25
c = 0
while(s>0):
  if (s%25)%2==0:
    c+=s%25
  s//=25
print(c)