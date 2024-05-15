# chars = 'АВЕСТ'
# count = 1


# for i in chars:
#   for j in chars:
#     for k in chars:
#       for v in chars:
#         for w in chars:
#           word = i+j+k+v+w
#           if(word=='СВЕТА'):
#             print(count)
#           count+=1


# count=0
# for a in '012345678': 
#   for b in '012345678':
#     for c in '012345678':
#       for d in '012345678':
#         for e in '012345678':
#           r = a+b+c+d+e
#           if( r[0] not in '01357' and r[-1] not in '18' and r.count('3')<2 ):
#             count+=1

# from itertools import *
# from n5 import change_not
# # все 17-ричные цифры, которые не являются простыми
# abc = (0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16)

# # все цифры различны, поэтому используем
# # permutations вместо product
# k = sum(
#     p[0] != 0 and p[0] % 2 == 0
#     for p in permutations(abc, r=6)
# )

# print(k)

# from itertools import *
# count=0
# a0='2468'
# a1='1357'
# for x in product(a0, a1, a0, a1, a0, a1, a0, a1, a0):
#   s=''.join(x)
#   if(all(s.count(i)<=3 for i in s)):
#     count+=1

# print(count*2)

#-----------4588-------------------
# from itertools import *
# count=0
# for n in product('01234567', repeat=5):
#   s=''.join(n)
#   if all(s.count('6')==1 and not(i+'6' in s) and not('6'+i in s) for i in '1357'):
#     count+=1
# print(count)


#-----------10120-------------------
# chars = set('0 1 4 6 8 9 10 12 14 16 16'.split())
# c=0
# for i in set('4 6 8 10 12 14 16'.split()):
#   for j in chars-set((i,)):
#     for k in chars-set((i,j)):
#       for v in chars-set((i,j,k)):
#         for w in chars-set((i,j,k,v)):
#           c+=1
# print(c)


# chars='ЕИКРСУ'
# c=1
# count=0
# for i,j,k,l,m,n in product(chars, repeat=6):
#   s = i+j+k+l+m+n
#   if(c%2==0 and i!='К' and s.count('Е')+s.count('И') + s.count('Р')<=2):
#     print(c, s)
#     count+=1
#   c+=1
# print(count)

#-----------9861-------------------
# from itertools import product

# count=0
# chars = '0 1 * 3 * 5 * 7 * 9'
# for s in product(chars.split(), repeat=6):

#   if (s.count('*') + s.count('0'))<=2 and sum(int(i) for i in s if i!='*')%2==0 and s[0]!='0':
#     count+=1
# print(count)

chars = '0123456'
c_chars = '246'
count=0
for a in chars[1:]:
  for b in chars:
    for c in chars:
      for d in chars:
        for e in chars:
          s = a+b+c+d+e
          if s.count('0')==1 and sum(s.count(x) for x in c_chars)%2==0:
            count+=1
print(count)
          