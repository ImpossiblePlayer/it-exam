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
#       c = s.rfind(i) - s.find(i)
#       max_s=max(max_s, c)
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
#   c = max_str.count(i)
#   if(c>max_count):
#     max_count=c
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
f = open('24.txt').readline()
count = f.count('A')
d = f.count('AA')
print(count*(count-1)//2 - sum(f[i:i+2] =='AA' for i in range(len(f)-1)))