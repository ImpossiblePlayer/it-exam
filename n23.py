# def f(n, k):
#   if n>k or n==12:
#     return 0
#   if n==k:
#     return 1
#   return f(n-3, k) + f(n*2, k) + f(n**2, k)



# def f(n, k, count, max_count):
#   if count > max_count:
#     return 0
#   if n>k:
#     return 0
#   if n==k and count==max_count:
#     return 1
#   return f(n+1, k, count+1, max_count) + f(n+5, k, count+1, max_count) + f(n*3, k, count+1, max_count)

# for i in range(2, 10):
#   print(i, f(1, 227, 0, i))


# def f(n, k, count):
#   if n>k or count>7:
#     return 0
#   if n==k and count==7:
#     return 1
#   return f(n+1, k, count+1) + f(n+5, k, count+1) + f(n*3, k, count+1)

# count=0
# for i in range(1, 4375):
#   if(f(1, i, 0)):
#     count+=1
# print(count)


# def f(n, s, count):
#   if count>7:
#     return set()
#   if count==7:
#     s.add(n)
#     return s
#   return f(n+1, s, count+1) | f(n+5, s, count+1) | f(n*3, s, count+1)

# print(len(f(1, set(), 0)))


# def f(n, k, count): # для четверичных чисел
#   if n>k:
#     return 0
#   if n==k:
#     return 1
#   return f(n+2, k, count+1) + f(n+3, k, count+1) + f(n*4, k, count+1)
# print(f(1, 16, 0))


# def f(n, k, count):
#   if n>k:
#     return 0
#   if n==21:
#     return 0
#   if n==k:
#     return 1
#   return f(n+1, k, count+1) + f(n+4, k, count+1) + f(2 - n%2 + 2*n, k, count+1)
# print(f(2, 11, 0) * f(11, 26, 0))

# def f(n, k, count):
#   if n>k:
#     return 0
#   if count>1:
#     return 0
#   if n==k:
#     return 1
#   return f(n+1, k, 0) + f(n*2, k, 0) + f(n+2, k, count+1)
# print(f(1, 12, 0))


# def f(n, k, count):
#   if n>k:
#     return 0
#   if count>2:
#     return 0
#   if n==k:
#     return 1
#   if(n%2==1): return f(n+2, k, count) + f(n*2,  k, count)
#   if(n%2==0): return f(n+2, k, count) + f(n*2+1,  k, count+1)
# print(f(2, 35, 0))


# def f(n, k, count):
#   if count>11:
#     return set()
#   if count==11 and n<0:
#     k.add(n)
#     return k
#   return f(n-2, k, count+1) | f(n*(-3),  k, count+1)
# print(len(f(91, set(), 0)))


# def f(n, k, m_count, s_count):
#   if n>k:
#     return 0
#   if n==k and m_count>s_count:
#     return 1
#   return f(n+1, k, m_count, s_count+1) + f(n*2, k, m_count+1, s_count) + f(n*3, k, m_count+1, s_count)
# print(f(1, 157, 0, 0))


# def f(n, k, count):
#   if n>k or count>5:
#     return 0
#   if n==k and count==5:
#     return 1
#   if(sum([int(i) for i in str(n)]) == 14):
#     count+=1
#   return f(n+2, k, count) + f(n*3, k, count) + f(n*4, k, count)
# print(f(1, 600, 0))


# nums = [17, 19, 23, 29, 31]
# def f(n, k, count):
#   if n>k or count>3:
#     return 0
#   if n==k and count==3:
#     return 1
#   if(n in nums):
#     count+=1
#   return f(n+2, k, count) + f(n+3, k, count)
# print(f(15, 34, 0))


# def f(n, k):
#   if n>k:
#     return 0
#   if n==k:
#     return 1
#   summ = 0
#   if n%10!=0:
#     num = n + n%10
#     summ += f(num, k)
#   if n>=20:
#     num=n*(n//10)
#     summ += f(num, k)
#   if n%10 != n//10:
#     num = n + max(n//10, n%10) - min(n//10, n%10)
#     summ += f(num, k)
#   return summ
# print(f(21, 62))

# def f(n, k):
#   if n<k:
#     return 0
#   if n==k:
#     return 1
#   return f(n-1, k) + f(n//2, k)
# print(f(30, 12)*f(12, 1))

# from functools import cache
# @cache
# def f(n, k, flag, p1, p2, p3):
#   if(p1!=0 and p2!=0 and p3!=0 and sum((p1, p2, p3))%11==0):
#     flag=1
#   if(n>=k):
#     return flag and n==k
#   return f(n+2, k, flag, n, p1, p2) + f(n*3, k, flag, n, p1, p2) + f(n*4, k, flag, n, p1, p2)
# print(f(1, 600, 0, 0, 0, 0))

from functools import lru_cache


# @lru_cache(maxsize=None)
# def f(n, k, c):
#   if(n>k or c==2 or n==23):
#     return 0
#   if(n==k):
#     return 1
#   return f(n+1, k, c+1) + f(n+2, k, 0) + f(n*2, k, 0)
# print(f(3, 9, 0) * f(11, 79, 0) + f(3, 8, 0) * f(11, 79, 1)+ f(3, 5, 0)*f(11, 79, 1))

# @lru_cache(maxsize=None)
# def f(n, k, c):
#   if(n>k or c==2 or n==33):
#     return 0
#   if(n==k):
#     return 1
#   return f(n+1, k, 0) + f(n+3, k, 0) + f(n*2, k, c+1)
# print(f(2, 9, 0) * f(18, 51, 1) + f(2, 17, 0) * f(18, 51, 0)+ f(2, 15, 0)*f(18, 51, 0))

#-----------1760-----------------------
# @lru_cache(maxsize=None)
# def f1(n, k):
#   if(n>k or n==17):
#     return 0
#   if(n==k):
#     return 1
#   return f1(n+2, k) + f1(n+3, k) + f1(n+5, k)
# @lru_cache(maxsize=None)
# def f2(n, k):
#   if(n>k or n==13):
#     return 0
#   if(n==k):
#     return 1
#   return f2(n+2, k) + f2(n+3, k) + f2(n+5, k)
# print(f1(5, 13)*f1(13, 25) + f2(5, 17)*f2(17, 25))
#--------------------------------------

# @lru_cache(maxsize=None)
# def f(n, k, c):
#   if(n>k or c>100):
#     return 10**20
#   if(n==k):
#     return c
#   return min(f(n+1, k, c+1), f(n*2, k, c+1), f(n*3, k, c+1))
# print(f(1, 32718, 0))

# @lru_cache(maxsize=None)
# def f(n, k):
#   if(n>k):
#     return 0
#   if(n==k):
#     return 1
#   x =  f(n+5, k) + f(n+10, k)
#   if(n%10 not in [0, 1]):
#     x+=f(n*(n%10), k)
#   return x
# print(f(10, 220))

# @lru_cache(maxsize=None)
# def f(x, y, k):
#   if(x+y>k):
#     return 0
#   if(x+y==k):
#     return 1
#   return f(x+y, y, k) + f(x, x+y, k)
# print(f(1, 1, 88))

@lru_cache(None)
def f(n, k, c1='', c2='', flag=False):
  if n > k:
    return 0
  if n == k:
    return flag
  x = f(n+1, k, 'A', c1, flag)+f(n*3, k, 'B', c1, flag)
  if(not flag): flag= (c2 + c1 + 'C' == 'CAC')
  x += f(n+5, k, 'C', c1, flag)
  return x
print(f(3, 69))