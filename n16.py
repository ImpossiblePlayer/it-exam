# from functools import lru_cache
# @lru_cache(maxsize=None)
# def f(n):
#   if(n>=2025): return n
#   return f(n+1) - f(n+2) + 7

# for i in range(2024, 14, -1):
#   f(i)

# print(f(15) - f(24))


# def f(n):
#   print( n ) 
#   if n > 0: 
#     d = (n%10 + 
#         f(n//10))
#     print(d)
#     return d
#   else: 
#     return 0

# for i in range(10000):
#   n = i//10
#   if(n>51):
#     print(i, f(n))
#     break


# def f(n,m):
#  if m == 0:
#    return n
#  else:
#    return f(m,n%m)

# nums = set()
# for n in range(100, 1001):
#   for m in range(100, 1001):
#     num = f(n,m)
#     if(num == 30):
#       nums.add(n)

# print(nums)
# print(len(nums))

# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#   if n < 3:
#     return n
#   if n > 2 and n % 2 == 1:
#     return f(n-1) + f(n-2) + 1
#   if n > 2 and n % 2 == 0:
#     sum_ = 0
#     for i in range(1, (n-1)+1):
#       sum_ += f(i)
#     return sum_
# print(f(38))


# def F(n, c=0):
#   # print('*')
#   c+=1
#   if n>1:
#     c+=F(n-2)
#     c+=F(n//2)
#     # print('*')
#     c+=1
#   # print('*')
#   c+=1
#   return c

# print(F(127))

from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10000)
@lru_cache(maxsize=None)
def f(n):
  if n==1:
    return 2
  x = f(n-1)
  if(x<7555444):
    return x+6
  return x-7555444
ans = []
# for i in range(1000,7555446):
#   x = f(i)
#   if(x):
#     ans.append((i,x))
# print(max(i[1] for i in ans))
print(f(7555444))