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

answer = set()
def f(c, step):
  if(step==13):
    answer.add(c)
  else:
    f(c-3, step+1)
    f(c*(-3), step+1)
f(333, 0)
print(len([i for i in answer if i<0]))