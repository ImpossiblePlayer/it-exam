# for i in '0123456789abcdefghi':
#   sum = int(f'98{i}79641', 19) + int(f'36{i}14', 19) + int(f'73{i}4', 19)

#   if(sum%18==0):
#     print(int(i,19), sum//18)

def change_notation(n, k):
  chars = '0123456789abcd'
  r = ""
  while(n>0):
    r += chars[n%k]
    n//=k
  return r[::-1]

s = 283**382 + 9**15 + 2**3
k = change_notation(s, 14)
b = k.count('b')
c = k.count('c')
print(b-c)

# answer = []
# for x in range(37):
#   for y in range(37):
#     a = 1*37**7 + 2*37**6 + x*37**5 + 6*37**4 + 4*37**3 + 3*37**2 + y*37 + 7
#     if(a%36==0):
#       answer.append(37*y + x)
# print(max(answer))
