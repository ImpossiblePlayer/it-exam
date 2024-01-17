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

def f(n):
  if n >= 2073:
    return n+3
  return n + f(n+2) - f(n+3)
print(f(2070)+f(2069))