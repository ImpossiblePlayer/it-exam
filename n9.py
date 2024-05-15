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



# file = open('9.txt').readlines()
# nums = [tuple(map(int, i.split())) for i in file]
# s = 0
# for i in range(len(nums)):
#   a = nums[i]
#   if(len(set(a))!=len(a)):
#     continue
#   n = {}
#   for j in a:
#     n[j]=n.get(j,0)+1
#   if all(sum(1 for v in n.values() if v>1) < len(a)) and sum(k for k,v in n.items() if v>1)/sum(1 for k,v in n.items() if v>1) > sum(a)/len(a):
#     s+=(i+1)


f = open('9.txt').readlines()
nums = [tuple(map(int, i.split())) for i in f]

s=0
for r in range(len(nums)):
  i = nums[r]
  if sum(i.count(j)==1 for j in i)==4 and sum(i.count(j)==3 for j in i)==3:
    for j in i:
      if(i.count(j)==3 and j not in (min(i), max(i))):
        s+=r+1
print(s)
