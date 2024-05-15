from fnmatch import *


def simple(n):
  if(n<2): return False
  i=2
  while i*i<=n:
    if(n%i==0):
      return False # число не простое
    i+=1
  return True

def friendly(n):
  d = dividers2(n)
  s = sum(d)
  d2 = dividers2(s)
  s2 = sum(d2)
  if(s2==n and s>n):
    return s
  return False

def growing(n):
  s=str(n)
  for i in range(len(s)-1):
    if(s[i] > s[i+1]):
      return False
  return True

def excess(n):
  d = dividers2(n)
  if(sum(d)> n): return True
  return False

def dividers2(n):
  d = []
  i=2
  while i*i<n:
    if(n%(i)==0):
      d.append(i)
      d.append(n//i)
    i+=1
  if(i*i==n):
    d.append(i)
  return d

def dividersC(n):
  d = list()
  i=2
  count=0
  while i*i<n and count<6:
    if(n%(i)==0):
      d.append(i)
      d.append(n//i)
      count+=2
    i+=1
  if(i*i==n):
    d.append(i)
  # if(count==2):
  #   d.append(n//d[len(d)//2-1])
  # s = sum(d[])
  if(len(d)<3):
    return 0
  d.sort()
  s = sum(d[-3:])
  return s

def dividers3(n):
  i = 2
  while i*i<n:
    if(n%(i)==0):
      d = dividers2(n//i)
      if(simple(i) and d and (n//i)%i!=0 and d[0]%10 == d[1]%10 and d[0]%10 == i%10):
        return True
      return False
    i+=1


def mask(n):
  s = str(n)
  if (s[0]!='1' or int(s[1])%2!=0 or s[2:6]!='2157' or any(int(i)%2!=1 for i in s[5:-1]) or s[-1]!='4'):
    return False
  if (s[0]=='1' and int(s[1])%2==0 and s[2:6]=='2157' and all(int(i)%2==1 for i in s[5:-1]) and s[-1]=='4'):
    return True
# max_num = 0
# count=0
# for i in range(2, 20001):
#   d = excess(i)
#   if(d): count+=1
# print(count)


# for i in range(8432*133, 10**10+1, 133):
#   if(mask(i)):
#     print(i, i//133)


# i =10_000_000
# count=0
# while(count<5):
#   d = dividersC(i)
#   if(simple(d)):
#     count+=1
#     print(i, d)
#   i+=1


count=0
summ=0
ans = []
for i in range(1024, 10**9+1, 1024):
  if(fnmatch(str(i), '3?5?21*4?')):
    # s = sum(int(x) for x in str(i))
    ans.append(i)
ans.sort()
print(ans)
for i in ans:
  print(i, i//1024)


# count=0
# summ=0
# ans = []
# for i in range(100, 10**6):
#   d = dividers2(i)
#   if not d:
#     continue
#   if not(fnmatch(str(max(d)), '4*')):
#     continue
#   n = [i for i in d if fnmatch(str(i), '4*')]
#   if len(n)!=24:
#     continue
#   print(i, max(n))


# c=0
# i=1273547
# while(c<5):
#   m = sum(dividers2(i))
#   if simple(m%100_000):
#     print(i, m)
#     c+=1
#   i+=1


# count=0
# summ=0
# ans = []
# i=400_000_000
# for i in range(1_200_000, 0, -1):
#   d = sorted(dividers2(i))
#   if len(d)<3:
#     continue
#   # n = [i for i in d if i%10==0 and i//10 in list(range(100, 1000)) ]
#   p = sum(d[-3:])
#   if(p%2022==0 and p!=i):
#     count+=1
#     print(i, p)