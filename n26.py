# f = open('26.txt').readlines()
# lenght = int(f[0])
# nums = [int(i) for i in f[1:]]
# answer=[]
# for i in range(lenght):
#   for j in range(i+1, lenght):
#     # for k in range(j+1, lenght):
#     if nums[i]%2!=0 and nums[j]%2!=0:
#       c = nums[i] + nums[j]
#       answer.append(c//2)
# nums.sort()
# answer.sort()
# j=0
# count=0
# max_ans=0
# for i in range(len(answer)):
#   while answer[i]>nums[j]:
#     j+=1
#   if answer[i]==nums[j]:
#     count+=1
#     max_ans=max(max_ans, nums[j])
# print(count, max_ans)


# f = open('26.txt').readlines()
# n, mass = map(int, f[0].split())
# nums = [int(i) for i in f[1:]]
# nums.sort(reverse=True)
# g = 0
# count=0
# while(nums):
#   m=mass
#   i=0
#   while(m>0 and i<len(nums)):
#     if(nums[i]<=m):
#       m-=nums.pop(i)
#     else:
#       i+=1
#   count+=1
#   g=mass-m
# print(count, g)


# f = open('26.txt').readlines()
# lenght = int(f[0])
# nums = [int(i) for i in f[1:]]
# answer=[]
# for i in range(lenght):
#   for j in range(i+1, lenght):
#     # for k in range(j+1, lenght):
#     c = nums[i] + nums[j]
#     if (c%2)==0:
#       answer.append(c//2)
# nums.sort()
# answer.sort()
# j=0
# count=0
# min_ans=10**100
# for i in range(len(answer)):
#   while answer[i]>nums[j]:
#     j+=1
#   # greater = lenght - j - (nums[j]==j)
#   # if (greater>=lenght//4) and j>=lenght//2:
#   k1 = answer[i] - nums[j-1]
#   k2 = nums[j] - answer[i]
#   if min(k1, k2)==5:
#     count+=1
#     min_ans=min(min_ans, answer[i])
# print(count, min_ans)


# f = open('26.txt').readlines()
# lenght = int(f[0])
# nums = [int(i) for i in f[1:]]
# nums.sort()

# count=0
# max_ans=0
# for i in range(lenght-101):
#   for j in range(i+101, lenght):
#     if(nums[i]+nums[j])%2==0:
#       count+=1
#       max_ans=max(max_ans, (nums[i]+nums[j])//2)
# print(count, max_ans)


# ---------47--------------------------
# f = open('26.txt').readlines()
# lenght = int(f[0])
# nums = [int(i) for i in f[1:]]
# avgs=[]
# for i in range(lenght):
#   for j in range(i+1, lenght):
#     # for k in range(j+1, lenght):
#     c = nums[i] + nums[j]
#     avgs.append(c//2)
# nums.sort()
# avgs.sort()
# j=0
# count=0
# max_ans=0
# for i in range(len(avgs)):
#   while avgs[i]>nums[j]:
#     j+=1
#   less = j + (nums[j]==j)
#   if(less!=0 and less%100 ==0):
#     count+=1
#     max_ans=max(max_ans, less)
# print(count, max_ans)
# --------------------------------------


#---------49-----------------------------
# f = open('26.txt').readlines()
# lenght = int(f[0])
# nums = [int(i) for i in f[1:]]
# answer=[]
# for i in range(lenght):
#   for j in range(i+1, lenght):
#     # for k in range(j+1, lenght):
#     c = nums[i] + nums[j]
#     if (c%2)==0:
#       answer.append(c//2)
# nums.sort()
# answer.sort()
# j=0
# count=0
# max_ans=0
# for i in range(len(answer)):
#   while answer[i]>nums[j]:
#     j+=1
#   greater = lenght - j - (nums[j]==j)
#   if (greater>lenght//2):
#     # k1 = answer[i] - nums[j-1]
#     # k2 = nums[j] - answer[i]
#     # if min(k1, k2)==5:
#     count+=1
#     max_ans=max(max_ans, answer[i])
# print(count, max_ans)
#----------------------------------------

#---------52-----------------------------
# f = open('26.txt').readlines()
# lenght = int(f[0])
# nums = [int(i) for i in f[1:]]
# answer=[]
# nums.sort()
# for i in range(lenght-1):
#   for j in range(i+1, i+100+2):
#     if(j<lenght):
#     # for k in range(j+1, lenght):
#       c = nums[i] + nums[j]
#       if c%10==0:
#         answer.append(c//2)
# answer.sort()
# min_ans = answer[0]
# print(len(answer), min_ans)
#----------------------------------------

#---------54-----------------------------
# f = open('26.txt').readlines()
# lenght = int(f[0])
# nums = [int(i) for i in f[1:]]
# answer=[]
# for i in range(lenght):
#   for j in range(i+1, lenght):
#     # for k in range(j+1, lenght):
#     if nums[i]%2==0 and nums[j]%2==0:
#       c = nums[i] + nums[j]
#       answer.append(c//2)
# nums.sort()
# answer.sort()
# j=0
# count=0
# min_ans=10**100
# for i in range(len(answer)):
#   while answer[i]>nums[j]:
#     j+=1
#   if answer[i]==nums[j]:
#     count+=1
#     min_ans=min(min_ans, nums[j])
# print(count, min_ans)
#----------------------------------------

#---------56-----------------------------
# f = open('26.txt').readlines()
# v, k, files_count = map(int, f[0].split())
# nums = [int(i) for i in f[1:]]
# nums.sort(reverse=True)
# disks = [v]*k
# other_files = []

# m = 0
# for i in range(len(nums)):
#   c=0
#   while(c<k):
#     if nums[i] <= disks[m]:
#       disks[m]-=nums[i]
#       m = (m+1)%k
#       break
#     else:
#       m = (m+1)%k
#       c+=1
#   if(c==k):
#     other_files.append(nums[i])
# print( sum(other_files), len(other_files))
#----------------------------------------

#---------59-----------------------------
# f = open('26.txt').readlines()
# n = int(f[0])
# nums = [list(map(int, i.split())) for i in f[1:]]

# rows = {}

# for i in nums:
#   rows[i[0]] = rows.get(i[0], []) + [i[1]]

# max_row = -1
# place_num = 0

# for i in rows.keys():
#   a = sorted(rows[i])
#   for j in range( len(a) - 1 ):
#     if(a[j+1] - a[j] == 3):
#       if(max_row < i):
#         max_row = i
#         place_num = a[j]+1
#       break
# print(max_row, place_num)
#----------------------------------------

#---------60-----------------------------
f = open('26.txt').readlines()
k, n = map(int, f[0].split())
specs = [int(i) for i in f[1:k+1]]

s={}

for i in f[k+1:]:
  b, c = map(int, i.split())
  s[c] = s.get(c, []) + [b]

max_k=0
min_student=0
e=0

for i in s.keys():
  students = sorted(s[i])
  if(len(students) > specs[i]):
    e += specs[i]
    if(max_k < len(students) / specs[i]):
      max_k = len(students) / specs[i]
      min_student = students[-1* specs[i]]
  else:
    e += len(students)

print(e, min_student)

#-----------КОНФЕРЕНЦ-ЗАЛ-----------------------
f = open('26.txt')
n = int(f.readline())
data = []
for line in f:
  start, end = map(int, line.split())
  data.append(end, start)
data.sort()

answer = [data[0][0], data[0][1]]
for i in range(1, n):
    if data[i][1] >= answer[-1][0]:
        answer.append((data[i][0], data[i][1], i))

max_break = 0
for i in range(answer[-2][2], n):
    max_break = max(max_break, answer[i][1] - answer[-2][0])

print(len(answer), max_break)