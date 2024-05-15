# f = open('24_934.txt').readline()
# # def fn(n):

# chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# nums = []
# count = 1
# max_count = 0

# for i in range(1, len(f)):
#   if(f[i]==f[i-1]):
#     count+=1
#   else:
#     nums.append(count)
#     count=1
#     if(f[i]<f[i-1]):
#       nums.append(0)

# nums.append(count)

# for i in range(len(nums)-2):
#   if(nums[i]>0 and nums[i+1]>0 and nums[i+2]>0):
#     max_count = max(max_count, nums[i] + nums[i+1] + nums[i+2])

# print(max_count)


# f = open('24_1147.txt').readline()
# # def fn(n):

# a=[0]*len(f)
# b=[0]*len(f)

# for i in range(len(f)-1):
#   for j in f[i]:
#     if(j=='A'):
#       a[i]+=1
#     if(j=='B'):
#       b[i]+=1

# count=0
# for i in range(len(f)-1):
#   if(1.05*a[i] <= b[i]):
#     count+=1

# print(count)


# f = open('24_1039.txt').readline()
# t = f[0]

# for i in range(1, len(f)):
#   if(f[i]==f[i-1] or ord(f[i]) - ord(f[i-1]) == 1 ):
#     t+=f[i]
#   else:
#     if(6<len(t)<11):
#       if(t[0]=='A' and t[-1]=='F'):

# chars = {}
# f = open('24_1147.txt').readline()
# for i in range(len(f)-3):
#   if(f[i+1]==f[i+2]):
#     if(f[i] in chars):
#       chars[f[i]]+=1
#     else:
#       chars[f[i]]=1

# max_count=0
# max_char=''
# for i in chars.keys():
#   if(chars[i]>max_count):
#     max_count=chars[i]
#     max_char=i

# print(max_char, max_count)


# f = open('24_1148.txt').readlines()

# max_count=0
# max_string=''
# for s in f:
#   count = s.count('Q')
#   if(count>=max_count):
#     max_count=count
#     max_string=s

# chars={}
# for i in max_string.rstrip():
#   chars[i] = chars.get(i, 0) + 1

# min_count=10**100
# min_char=''
# for i,j in chars.items():
#   if(j<min_count):
#     min_count=j
#     min_char=i
#   elif(j==min_count and i<min_char):
#     min_char=i

# count=0
# for i in f:
#   count+=i.count(min_char)

# print(min_char, count)
# print(max_string)


# f = open('24_1255.txt').readlines()
# max_s=0
# for s in f:
#   if(s.count('A')<25):
#     print(s)
#     for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#       c2 = s.rfind(i) - s.find(i)
#       max_s=max(max_s, c2)
# print(max_s)


# f = open('24_2428.txt').readline()
# lenght=0
# max_len=0
# for i in range(len(f)-2):
#   if(f[i:i+2]=='XYZ' or f[i-1:i+1]=='XYZ' or f[i-2:i]=='XYZ'):

# f = open('24_2428.txt').readline()
# m_index=0
# lenght=0
# max_length=0
# for i in f:
#   if(lenght%3==0 and i=='X'):
#     lenght+=1
#   elif(lenght%3==1 and i=='Y'):
#     lenght+=1
#   elif(lenght%3==2 and i=='Z'):
#     lenght+=1
#   else:
#     max_length=max(lenght-m_index, max_length)
#     if(i=='X'):
#       m_index=0
#       lenght=1
#     elif(i=='Y'):
#       m_index=1
#       lenght=2
#     elif(i=='Z'):
#       m_index=2
#       lenght=3
# print(max_length)

# f = open('24_2501.txt').readline()
# count=0
# for i in range(len(f)-4):
#   if(f[i]=='A' and f[i+2]=='A' and f[i+4]=='A'):
#     count+=1
# print(count)


# f = open('24.txt').readline()

# max_count=0
# max_char=''
# max_str=''
# for s in f:
#   count=0
#   for i in range(len(s)-1):
#     if(s[i]==s[i+1]):
#       count+=1
#       if(max_count<count):
#         max_count=count
#         max_str=s
#     else:
#       count=0
# max_count=0
# for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#   c2 = max_str.count(i)
#   if(c2>max_count):
#     max_count=c2
#     max_char=i
# count=0
# for s in f:
#   count+=s.count(max_char)
# print(max_char, count)

# f = f.replace('NPO', '*').replace('PNO', '*')
# f = f.replace('N', ' ').replace('P', ' ').replace('O', ' ')
# print(max(len(i) for i in f.split()))

#---------------11667--------------------
# f = open('24.txt').readline()
# indices = [i for i in range(len(f)-7) if f[i:i+8]=='INFINITY'] + [len(f)-6]
# amount = 1000
# max_len=0
# for i in range(amount+1, len(indices)):
#   max_len=max(max_len, indices[i]+6 - indices[i-amount-1])
# print(max_len)
#----------------------------------------

#---------------11636--------------------
# f = open('24.txt').readline()
# indices=[i for i in range(len(f)) if f[i]=='A']
# n = len(indices)
# count=0
# for i in range(n-1):
#   if(indices[i]!=indices[i+1]-1):
#     count+=n-i-1
#   else:
#     count+=n-i-2
# print(count)


#---------------9377--------------------
# f = open('24_9377.txt').readline().strip()
# print(f[-10:])
# # f = 'AS0256DG124FB2NHF1643GH124GG22ABCDF942AACV1'
# digits='1234567890'

# words=[]
# t = ''
# l = 0
# for i in f:
#   if(i in digits):
#     if(l!=0):
#       words.append(l)
#       l=0
#     t+=i
#   else:
#     if(t!=''):
#       words.append(t)
#       t=''
#     l+=1
# words.append(t)
# words.append(0)

# max_count=count=0
# for i in range(1, len(words), 2):
#   if words[i][0] != '0' and words[i][-1] in '02468':
#     try:
#       count+=len(words[i])
#       count+=words[i+1]
#     except:
#       print(words[i:i+2])
#   else:
#     max_count = max(count-words[i-1], max_count)
#     count=0
# max_count = max(count-words[i-1], max_count)
# print(max_count)


#---------------9169--------------------
# f = open('24.txt').readline()
# f = f.replace('FAT', '*').replace('BAD', '*')

# lens = [len(x) for x in f.split('*')[1:-1]]
# print(min(a+b for a,b in zip(lens, lens[1:])) + 9)

#---------------9552--------------------
# f = open('24_9552.txt').readline()
# chars = set(f)
# f=f.replace('PCSGO', 'PC CSGO').replace('PC', '**').replace('CSGO', '****')
# for c2 in chars:
#   f=f.replace(c2, ' ')
# print(f)
# print(max(map(len, f.split())))

#---------------9791--------------------
# f = open('24_9791.txt').readline()
# chars = set(f) - set('1234567890ABCDEF')

# for i in chars:
#   f=f.replace(i, ' ')

# print(max(map(len, f.split())))

#---------------4602--------------------
# f = open('24.txt').readline()
# f=f.replace('O', 'A').replace('C', 'B').replace('D', 'B')
# f=f.replace('BA', '*').replace('B', ' ').replace('A', ' ')
# print(max(len(i) for i in f.split()))

#---------------4602--------------------
# f = open('24.txt').readline()
# # f = 'AHAAHJYYAGHWAJSHGAKYGASHKLALWGPAYSGJ'
# k = 150
# s = f.split('Y')
# sums = []
# for i in range(len(s)-k):
#   sums.append(sum(len(i) for i in s[i:i+k+1])+k)
# print(max(sums))

#---------------13100--------------------
# f = open('24.txt').readline()
# e, b = 0, 0
# c2, d = 0, 0
# max_len=0
# while(e<len(f)):
#   while(c2<=2 and d<=2 and e<len(f)):
#     if(f[e]=='C'):
#       c2+=1
#     elif(f[e]=='D'):
#       d+=1
#     e+=1
#   max_len = max(max_len, e-b-1)
#   while(c2>2 or d>2):
#     if(f[b]=='C'):
#       c2-=1
#     if(f[b]=='D'):
#       d-=1
#     b+=1
# print(max_len)

#---------------13931--------------------
# f = open('24.txt').readline()
# f = f.replace('V', '0').replace('W', '1').replace('X', '2').replace('Y', '3').replace('Z', '4').replace('T', ' ').replace('U', ' ')
# words = [i for i in f.split() if len(i)>=10]
# print(words)
# max_len=0
# for i in words:
#   cur_len=1
#   for j in range(len(i)-1):
#     if(int(i[j+1]) == (int(i[j])+1)%5):
#       cur_len+=1
#     else:
#       print(i, cur_len)
#       max_len=max(max_len, cur_len)
#       cur_len=1
#   max_len=max(max_len, cur_len)
# print(max_len)

#---------------11954--------------------
# f = open('24_11954.txt').readline()
# x_ids= []
# for i in range(len(f)):
#   if(f[i]=='X'):
#     x_ids.append(i)
# min_len = 10**100

# for i in range(len(x_ids)-500+1):
#   if('Y' not in f[x_ids[i]:x_ids[i+499]]):
#     l = x_ids[i+499]-x_ids[i]+1
#     min_len = min(min_len, l)
# print(min_len)

#---------------10105--------------------
# f = open('24_10105.txt').readline()
# # f = 'AHAAHJYYAGHWAJSHGAKYGASHKLALWGPAYSGJ'
# k = 100
# s = f.split('T')
# sums = []
# for i in range(len(s)-k):
#   sums.append(sum(len(i) for i in s[i:i+k+1])+k)
# print(max(sums))

#---------------12476--------------------
# f = open('24_12476.txt').readline().strip()
# while('ROR' in f or 'ORO' in f):
#   f = f.replace('ROR', 'RO OR').replace('ORO', 'OR RO')
# f = f.replace('RO', '*').split()
# m = 0

# for s in f:
#   b, e = 0, 0
#   c2 = 0

#   while(c2<=21 and e<len(s)):
#     if(s[e])=='*':
#       c2+=1
#     e+=1
#   m = max(m, e-b+21)
#   while(c2>21 and e<len(s)):
#     if(s[b]=='*'):
#       c2-=1
#     b+=1
# print(m)

#---------------13085--------------------
# f = open('24_13085.txt').readline()
# e, b = 0, 0
# x, y = 0, 0
# max_len=0
# while(e<len(f)):
#   while(x<=1 and y<=1 and e<len(f)):
#     if(f[e]=='X'):
#       x+=1
#     elif(f[e]=='Y'):
#       y+=1
#     e+=1
#   max_len = max(max_len, e-b-1)
#   while(x>1 or y>1):
#     if(f[b]=='X'):
#       x-=1
#     if(f[b]=='Y'):
#       y-=1
#     b+=1
# print(max_len)

#---------------12476--------------------
# f = open('24_12254.txt').readline()
# f = f.replace('R', '0').replace('S', '1').replace('Q', '2').replace('B', ' ')
# words = [i for i in f.split() if '012' in i]
# max_len=0
# for i in words:
#   cur_len=1
#   for j in range(len(i)-1):
#     if(int(i[j+1]) == (int(i[j])+1)%3):
#       cur_len+=1
#     else:
#       max_len=max(max_len, cur_len)
#       cur_len=1
#   max_len=max(max_len, cur_len)
# print(max_len)

#---------------9791--------------------
# f = open('24_9791.txt').readline()
# chars = '123456789ABCDEF'

# bad_chars = 'GHIJKLMPNOPQRSTUVWXYX'

# for i in bad_chars:
#   f = f.replace(i, ' ')
# print(max(len(i) for i in f.split()))

#---------------9845--------------------
# f = open('24.txt').readline()
# f = f.replace('A', '*').replace('B', '*').replace('C', '*').replace('8', '#').replace('9', '#')

# tLen = 1
# maxLen = 1
# row = ''
# for i in range(1, len(f)):
#   if(f[i] != f[i-1]):
#     tLen += 1
#   else:
#     if(tLen > maxLen):
#       maxLen = tLen
#     tLen = 1
# print(maxLen)

#---------------8654--------------------
# f = open('24.txt').readline()
# start = 0
# max_len=0
# for i in range(len(f)-4):
#   if(f[i+1]=='B' and f[i+4]=='D'):
#     start = i
#   max_len = max(i+4-start, max_len)
# print(max_len)

#---------------8579--------------------
# f = open('24_8579.txt').readline()
# indices = []
# max_len=0
# for i in range(len(f)):
#   if(f[i] in '0123456789'):
#     indices.append(i)
# for i in range(len(indices)-1):
#   if(int(f[indices[i]])%2!=int(f[indices[i+1]])%2):
#     max_len=max(max_len, indices[i+1]-indices[i]+1)
# print(max_len)

#---------------8431--------------------
# f = open('24.txt').readline()
# # f = 'BADZXYZKLMENYZXXX'
# tLen = maxLen = 0
# for i in range(2, len(f)-3):
#   c1 = f[i:i+3]
#   c2 = f[i-1:i+2]
#   c3 = f[i-2:i+1]
#   if ('X' in c1 and 'Y' in c1 and 'Z' in c1) or ('X' in c2 and 'Y' in c2 and 'Z' in c2) or ('X' in c3 and 'Y' in c3 and 'Z' in c3):
#     tLen=0
#   else:
#     tLen+=1
#   maxLen = max(maxLen, tLen)
# print(maxLen)

#---------------8510--------------------
# f = open('24.txt').readline()
# while('NO' in f or 'ON' in f or 'NP' in f or 'PN' in f or 'OP' in f or 'PO' in f or 'NN' in f or 'OO' in f or 'PP' in f):
#   f = f.replace('NO', 'N O').replace('ON', 'O N').replace('NP', 'N P').replace('PN', 'P N').replace('OP', 'O P').replace('PO', 'P O').replace('NN', 'N N').replace('OO', 'O O').replace('PP', 'P P')
# print(max(len(i) for i in f.split()))

#---------------9552--------------------
# f = open('24.txt').readline()
# f = f.replace('CSGO', '****').replace('PC', '**')
# for i in f:
#   if(i!='*' and i!='#' and i!=' '):
#     f = f.replace(i, ' ')
# m = max(len(i) for i in f.split())
# print(m)

#---------------9169--------------------
# f = open('24.txt').readline()
# # f='SDFATFDBADZZSFATBADGHTBAD'
# f = f.replace('BAD', '*').replace('FAT', '*')
# min_len=10**100
# ids= []
# for i in range(len(f)):
#   if(f[i]=='*'):
#     ids.append(i)
# for i in range(len(ids)-2):
#   min_len=min(min_len, ids[i+2]-ids[i]+1+6)
# print(min_len)

#---------------9709--------------------
# f = open('24.txt').readline()
# f = f.replace('X', '0').replace('Y', '1').replace('Z', '2')
# max_len=0
# i=b=e=0
# last_c='2'
# while(i<len(f)):
#   e=i
#   while(f[e] in '012' and (int(f[e]) == (int(last_c)+1)%3)):
#     last_c=f[i]
#     e+=1
#   if(e-i>=2):
#     for i in range(b, e+1):
#       f.
#     i=e+1
#   i+=1
# # for i in range(len(f)-1):
# #   if  :
# #     e+=1
# #   else:
# #     b+=1
# #   if(b-e>=2):
# print(max(len(i) for i in f.split()))

#---------------10131--------------------
# s = open('24.txt').readline()

# # словарь для префиксов
# p = {}
# c = mx = 0

# for i in range(len(s)):
#     # если в строке равное количество букв
#     # A и B, то c будет равно 0
#     c += {'A': 1, 'B': -1}.get(s[i], 0)

#     # проверим особый случай, когда
#     # не надо убирать префикс
#     if c == 0: mx = i + 1

#     # ищем наибольшую длину с равным
#     # количеством букв A и B
#     mx = max(mx, i-p.get(c, 10**50))

#     # так как мы ищем максимальную длину,
#     # префикс должен быть минимальным,
#     # поэтому сохраняем первую строку
#     # с суммой c
#     p[c] = p.get(c, i)

# print(mx)

#---------------9882--------------------
f = open('24_9882.txt')
s = f.readline()
cc=cb=0
b=e=0
l = 10**10
while(e<len(s)):
  while((cc<127 or cb<127) and e<len(s)):
    if(s[e]=='C'):
      cc+=1
    if(s[e]=='B'):
      cb+=1
    e+=1
  while(cc>=127 and cb>=127 and b<e):
    if(s[b]=='C'):
      cc-=1
    if(s[b]=='B'):
      cb-=1
    b+=1
    l = min(l, e-b)
print(l)
