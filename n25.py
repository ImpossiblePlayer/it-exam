from fnmatch import *


def simple(n):
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
  if (len(s) > 6 and s[0]=='1' and int(s[1])%2==0 and s[2]=='2'
      and s[3]=='1' and s[4]=='5' and s[5]=='7' and s[-1]=='4'
      and (len(s) == 7 or all(int(x)%2!=0 for x in s[6:-1]))):
    return True
  return False
# max_num = 0
# count=0
# for i in range(2, 20001):
#   d = excess(i)
#   if(d): count+=1

# print(count)


count=0
summ=0
for i in range(161, 10**8+1, 161):
  if(fnmatch(str(i), '12*4?65')):
    print(i, i//161)
