def change_notation(n, k):
  r = ""
  while(n>0):
    r += str(n%k)
    n//=3
  
  return r[::-1]

# def f(n):
#   s = bin(n)[2:]

#   if n%5 == 0:
#     s = '1'+s+s[-2:]
#   else:
#     s = f'{s}{change_notation(n%3*5)}'
  
#   return int(s, 3)

# nums = [[i, f(i)] for i in range(1, 100000) if f(i)>133]

# print(sorted(nums, key=lambda x: x[1], reverse=True), sep='\n')



file = open('n9.txt')
count = 0
for s in file:
  a = [int(x) for x in s.split()]
  a.sort()
  if(len(set(a)) == 6):
    if(a[0]+a[-1]/2 > sum(a[1:-1])/4):
      count+=1
print(count)
