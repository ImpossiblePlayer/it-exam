#-----------КОНФЕРЕНЦ-ЗАЛ-----------------------
# f = open('26.txt')
# n = int(f.readline())
# data = []
# for line in f:
#   start, end = map(int, line.split())
#   data.append(end, start)
# data.sort()

# answer = [data[0][0], data[0][1]]
# for i in range(1, n):
#     if data[i][1] >= answer[-1][0]:
#         answer.append((data[i][0], data[i][1], i))

# max_break = 0
# for i in range(answer[-2][2], n):
#     max_break = max(max_break, answer[i][1] - answer[-2][0])

# print(len(answer), max_break)

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
# f = open('26.txt').readlines()
# k, n = map(int, f[0].split())
# specs = [int(i) for i in f[1:k+1]]

# s={}

# for i in f[k+1:]:
#   b, c = map(int, i.split())
#   s[c] = s.get(c, []) + [b]

# max_k=0
# min_student=0
# e=0

# for i in s.keys():
#   students = sorted(s[i])
#   if(len(students) > specs[i]):
#     e += specs[i]
#     if(max_k < len(students) / specs[i]):
#       max_k = len(students) / specs[i]
#       min_student = students[-1* specs[i]]
#   else:
#     e += len(students)

# print(e, min_student)

#-----------75-----------------------
# f = open('26.txt').readlines()
# n=int(f[0])
# nums = [list(map(int, i.split())) for i in f[1:]]

# intervals = [0]*1_000_000
# count=0

# for i in range(n):
#   start=nums[i][0]
#   end=nums[i][1]
#   intervals[start]+=1
#   intervals[end]-=1
# for i in range(1, len(intervals)):
#   intervals[i]+=intervals[i-1]
#   if(intervals[i]>0):
#     count+=1

# print(max(intervals))
# print(count)

#-----------66-----------------------
# f = open('26.txt').readlines()
# n, k = map(int, f[0].split())
# nums = [tuple(map(int, i.split())) for i in f[1:]]
# t_end = 86400000+2

# intervals = [0]*t_end
# count=0

# for i in range(n):
#   start=nums[i][0]
#   end=nums[i][1]
#   if(start<=k and (end==0 or k<=end)):
#     intervals[0]+=1
#   elif(k<=start<=k+t_end):
#     intervals[start-k]+=1

#   if(k<=end<=k+t_end):
#     intervals[end-k]-=1

# t_max = 0

# for i in range(1, len(intervals)):
#   intervals[i]+=intervals[i-1]
#   t_max=max(t_max, intervals[i])
# print(t_max, intervals.count(t_max))

#-----------67-----------------------
# f = open('26.txt').readlines()
# n, k = map(int, f[0].split())
# nums = [tuple(map(int, i.split())) for i in f[1:]]
# t_end = 86400000+1

# intervals = [0]*(t_end+1)
# count=0

# for i in range(n):
#   start=nums[i][0]
#   end=nums[i][1]
#   if(start<=k and (end==0 or k<=end)):
#     intervals[0]+=1
#   elif(k<=start<=k+t_end):
#     intervals[start-k]+=1

#   if(k<=end<=k+t_end):
#     intervals[end-k]-=1

# t_min = 10*1000

# for i in range(1, len(intervals)):
#   intervals[i]+=intervals[i-1]
#   t_min=min(t_min, intervals[i])
# print(t_min, intervals.count(t_min))

#-----------74-----------------------
# f = open('26_73.txt').readlines()
# n = int(f[0])
# nums = [tuple(map(int, i.split())) for i in f[1:]]
# nums.sort()

# rows = {}

# for i in range(n):
#   y=nums[i][0]
#   x=nums[i][1]
#   rows[y] = rows.get(y, set()) | {x}

# max_len=0
# max_row=10*100

# for i in rows:
#   row_len = 1
#   row = sorted(list(rows[i]))
#   for j in range(1, len(row)):
#     if(row[j]-row[j-1]==2):
#       row_len+=1
#       if(row_len>max_len):
#         max_len = row_len
#         max_row = i
#       elif(row_len==max_len):
#         max_len = row_len
#         max_row = min(i, max_row)
#     else:
#       row_len=1
# print(max_row, max_len)
# #-----------76-----------------------
# f = open('26.txt').readlines()
# l, n = map(int, f[0].split())
# nums = [tuple(map(int, i.split())) for i in f[1:]]

# timings = [0]*l

# for i in range(n):
#   start=nums[i][0]
#   end=nums[i][1]
#   for j in range(start, end):
#     timings[j]+=1

# max_break = 0
# break_sum = 0

# t_break=0

# for i in timings:
#   if(i==0):
#     break_sum+=1
#     t_break+=1
#   if(i==1):
#     max_break=max(max_break, t_break)
#     t_break=0
# print(break_sum, max_break)

#-----------77-----------------------
# f = open('26.txt').readlines()
# n = int( f[0])
# nums = set(tuple(map(int, i.split())) for i in f[1:])

# ans={}

# for i, j in nums:
#   ans[i]=ans.get(i, []) + [j]


# summ=sum(len(ans[i]) for i in ans)
# answ=max( (8-len(ans[i]), i) for i in ans)
# print(30*8 -summ, answ)


#-----------78-----------------------
# f = open('26.txt').readlines()
# n, start, end = map(int, f[0].split())

# times = list(tuple(map(int, i.split())) for i in f[1:])
# times.sort()

# ans=[start]
# end_t=0

# for i in times:
#   s = i[0]
#   e = i[1]

#   if(s<=ans[-1]):
#     end_t=max(end_t, e)
#   else:
#     ans.append(end_t)
#     end_t=e
#   if(ans[-1]>=end):
#     break

# print(len(ans)-1, ans[1]-ans[0])

#-----------79-----------------------
# f = open('26.txt').readlines()
# n, k = map(int, f[0].split())

# nums = list(tuple(map(int, i.split())) for i in f[1:])

# rows={}
# for i in nums:
#   rows[i[0]]=rows.get(i[0], [])+[i[1]]

# max_row=0
# min_id=10**100

# for i in rows:
#   row = sorted(rows[i])
#   for j in range(1, len(row)):
#     if(row[j]-row[j-1]==k+1):
#       min_id=row[j-1]+1
#       max_row=max(max_row, i)
#       break
# print(max_row, min_id)

#-----------69-----------------------
# f = open('26.txt').readlines()
# n = int(f[0])
# nums = [tuple(map(int, i.split())) for i in f[1:]]
# rows={}
# max_row=0
# max_id=0

# for i in nums:
#   rows[i[0]]=rows.get(i[0], [])+[i[1]]

# for i in sorted(rows):
#   row=[0]*100_000
#   for j in sorted(rows[i]):
#     row[j]=1
#   seats = ''.join(map(str, row)).split('0')
#   m = max(len(i) for i in seats)
#   if(max_row<=m):
#     max_row = m
#     max_id = max(max_id, i)
#     print(i, m)
# print(max_id, max_row)

#-----------89-----------------------
# f = open('26.txt').readlines()
# n = int(f[0])
# nums = list(map(int, f[1:]))
# nums.sort(reverse=True)
# boxes = [nums[0]]

# for i in nums[1:]:
#   if(boxes[-1]-i>2):
#     boxes.append(i)
# print(len(boxes), boxes[-1])

#-----------89-----------------------
# f = open('26.txt').readlines()
# n, d = list(map(int, f[0].split()))
# nums = list(map(int, f[1:]))
# nums.sort(reverse=True)
# count=0
# bad_boxes = []

# i=0
# while(nums):
#   biggest = nums.pop(0)
#   l = len(nums)
#   for i in range(len(nums)):
#     if(biggest + nums[i]<=d):
#       count+=1
#       nums.pop(i)
#       break
#   if(l==len(nums)):
#     bad_boxes.append(biggest)
# print(count, sum(bad_boxes))

#-----------71-----------------------
# f = open('26.txt').readlines()
# n, s = map(int, f[0].split())
# nums = [tuple(map(int, i.split())) for i in f[1:]]
# boxes = {}
# left=[]
# summ = 0

# for i in nums:
#   boxes[i[0]]=boxes.get(i[0], [])+[i[1]]
# for i in boxes:
#   m = s
#   bType = sorted(boxes[i])
#   b = 0
#   while(b<len(bType) and m>0):
#     if(m>=bType[b]):
#       m-=bType[b]
#       del bType[b]
#     else:
#       b+=1
#   summ +=len(bType)
#   left.append(i)

# left.sort(reverse=True)
# print(list(i for i in left if i==2000251), summ)

#-----------84-----------------------
# f = open('26.txt').readlines()
# n = int(f[0])
# groups = sorted(list(map(int, f[1].split())))
# rooms = sorted(list(map(int, f[2].split())))
# nums = []
# j=0
# for r in rooms:
#   while j<n and groups[j]<=r:
#     j+=1
#   nums.append(j)
# c=1
# for i in range(n):
#   c = c*(nums[i]-i)%100000007

# print(c, nums[0])
#-----------90-----------------------
# import math
# f = open('26.txt').readlines()
# n = int(f[0])
# nums = list(map(int, f[1:]))
# nums.sort()
# l = math.ceil(len(nums)*3/4)
# goods = []

# for i in range(0, l, 3):
#   goods+= [*nums[i:i+3], 0]
# print(goods[:50])
# for i in range(l, len(nums)):
#   goods[(i-l+1)*4-1] += nums[i]*0.5
# print(sum(goods), sum(nums))

#-----------92-----------------------
# f = open('26.txt').readlines()
# n = int(f[0])
# print(f)
# nums = list(i.strip().split() for i in f[1:])
# rows = [[0]*10000]*10000

# for i in nums:
#   if(i[2]=='-'):
#     rows[int(i[0])][int(i[1])]=0
#   else:
#     rows[int(i[0])][int(i[1])]=1
# print(max(len(j) for j in i.split() for i in rows))

#-----------7828-----------------------
# f = open('26.txt').readlines()
# n = int(f[0])
# nums = sorted(list(map(int, f[1:])), reverse=True)
# boxes = [[nums[0]]]
# count=1
# for i in range(1, n):
#   f=True
#   for b in boxes:
#     if(b[-1]-nums[i]>=5):
#       b.append(nums[i])
#       f=False
#       break
#   if(f):
#     boxes.append([nums[i]])
# print(len(boxes), max(len(i) for i in boxes))

#-----------12478-----------------------
# f = open('26_12478.txt').readlines()
# n, start, end = map(int, f[0].split())
# nums = sorted(tuple(map(int, i.split())) for i in f[1:])
# c=0
# m = -1
# people = [start]
# i=0
# while(people[-1]<end and i<n):
#   m_r = nums[i][1]
#   while(i<n and nums[i][0]<=people[-1]):
#     m_r = max(m_r, nums[i][1])
#     i+=1
#   people.append(m_r)

# print(len(people)-1, people[1]-people[0])  
# print(people)

#-----------12478-----------------------
# f = open('26.txt')
# n = int(f.readline())

# # отсортируем входные данные
# # в порядке неубывания
# a = sorted(int(x) for x in f)
# count = mx = 0
# # будем перебирать первые две стороны треугольника
# for i in range(n-2):
#     k = i + 2
#     for j in range(i+1, n-1):
#         mx_side = 0
#         # очевидно, что a[r] > a[l] и a[r] > a[i]
#         # поэтому проверяем только одно неравенство
#         # треуголника (a < b + c)
#         # также очевидно, что если a[r] >= a[i] + a[l],
#         # треугольник не будет существовать, поэтому
#         # можно сразу выйти из цикла
#         while k < n and a[i] + a[j] > a[k]:
#             # так как мы ищем максимальную сумму,
#             # будем сохранять максимальную длину стороны
#             mx_side = max(mx_side, a[k])
#             k += 1
#         # все стороны a[k] (k in (l; r)) будут образовывать
#         # необходимый треугольник
#         count += k - j - 1
#         mx = max(mx, a[i] + a[j] + mx_side)
# print(count, mx)

#-----------13395-----------------------
# f = open('26.3_13395.txt')
# n, m = map(int, f.readline().split())
# boxes = []
# keys = []
# sets = []
# for _ in range(m):
#   b, k = map(int, f.readline().split())
#   boxes.append(b)
#   keys.append(k)
# for _ in range(n-m): # надо проверять числа с разной четностью, поскольку первое число может быть выгоднее при другой четности
#   boxes.append(int(f.readline()))
# boxes.sort(reverse=True)
# id=0
# while(boxes[id] not in keys or boxes[id]%2!=0):
#   id+=1
# sets = [boxes[id]]

# for i in range(id+1, n):
#   b = boxes[i]
#   if b+5<=sets[-1] and (b-sets[-1])%2!=0 and b in keys:
#     sets.append(b)
# print(len(sets), sets[-1], sets[0])

#-----------14959-----------------------
# f = open('26_14959.txt')
# k, n = map(int, f.readline().split())
# a = []
# for _ in range(n):
#   x, y = map(int, f.readline().split())
#   a.append((x, x+y))
# tasks = []
# a.sort(key= lambda x: x[1])
# t = [a[0][1]]
# for i in range(1, n):
#   if t[-1]<=a[i][0]:
#     t.append(a[i][1])
# mn = 10**20
# for i in range(n):
#   if(a[i][0]>=t[-2]):
#     mn = min(mn, a[i][0])
# print(len(t)*k, mn)

#-----------13394-----------------------
# import math
# f = open('26.6_13394.txt')
# n = int(f.readline())
# a = [int(f.readline()) for _ in range(n)]
# a.sort(reverse=True)
# s = a[n-1]
# for i in range(0, n-1, 3):
#   s += math.ceil(a[i]+a[i+1] + (a[i+2]*0.25 if a[i+2]>350 else a[i+2]))

# c = sum(1 for i in range(n) if a[i]>350)//3
# a1 = [a[i] for i in range(n) if a[i]>350]
# s2 = sum(a[i] for i in range(n) if a[i]<=350)
# s1 = math.ceil(sum(a1[-c:])*0.25) + sum(a1[:-c]) + s2
# print(s, s1)

#-----------13101-----------------------
# f = open('26_13101.txt')
# n = int(f.readline())
# a0 = []
# a1 = [0]
# a2 = [0]
# q1 = q2 = 1
# c=0
# k=14
# s = [tuple(map(int, f.readline().split())) for _ in range(n)]
# s.sort()
# for i in range(n):
#   x, y, z = s[i]
#   print(a1, a2)
#   while(q1< len(a1) and a1[q1]<=x):
#     q1+=1
#   while(q2< len(a2) and a2[q2]<=x):
#     q2+=1
#   print(q1,q2)
#   if(z) == 2:
#     if(len(a2)-q2<k):
#       a2.append(max(y+a2[-1], y+x))
#     else: c+=1
#   elif(z) == 1:
#     if(len(a1)-q1<k):
#       a1.append(max(y+a1[-1], y+x))
#     else: c+=1
#   else:
#     if(len(a1)-q1 <= len(a2)-q2):
#       if(len(a1)-q1<k):
#         a1.append(max(y+a1[-1], y+x))
#       else: c+=1
#     else:
#       if(len(a2)-q2<k):
#         a2.append(max(y+a2[-1], y+x))
#       else: c+=1
# print(len(a2)-1, c)

#-----------11605-----------------------
# f = open('26_11605.txt')
# n, k = map(int, f.readline().split())
# a = [tuple(map(int,f.readline().split())) for _ in range(n)]
# c = last_lamp = i = 0
# a.sort()
# while(last_lamp<k):
#   j = a[i][1]
#   while i < n and a[i][0]<=last_lamp+1:
#     j = max(j, a[i][1])
#     i+=1
#   c+=1
#   last_lamp = j
# print(n-c, sum((i[0]<=k and i[1]>=k) for i in a))

#-----------3088-----------------------
# f = open('26_3088.txt')
# n = int(f.readline())
# a = [tuple(map(int, f.readline().split())) for _ in range(n)]
# a.sort()
# t=(16*60+1)
# times = [0]*t
# goods = {}
# print(a)
# for i in range(n):
#   goods[a[i][1]] = goods.get(a[i][1], []) + [a[i][0]]
#   if(len(goods[a[i][1]])%2==0):
#     times[a[i][0]]+=1
# m=0
# sm=0
# si=0
# for i in range(t-60):
#   m = max(m, sum(times[i:i+60]))
# for k, v in goods.items():
#   s_ = 0
#   for i in range(1, len(v),2):
#     s_+=v[i]-v[i-1]
#   if(s_/len(v)> sm):
#     sm = s_/len(v)
#     si = k
# print(m, si)

#------------476-----------------------
# f = open('26_476.txt')
# n = int(f.readline())
# a = sorted(int(i) for i in f)

# m = 0.6*sum(a)
# s1 = 0.8*sum(a[n-n//5:])
# s2 = sum(a[:n-n//5])
# print(s1, (m-s1)/s2*a[0])

#------------507-----------------------
# f = open('26_507.txt')
# n = int(f.readline())
# a1 = sorted(int(i) for i in f)
# a2 = a1.copy()
# for i in range(n*7//10):
#   a1[i]*=0.7
# for i in range(n*7//10, n):
#   a1[i]*=0.6

# for i in range(n*5//10):
#   a1[i]*=0.6
# for i in range(n*5//10, n):
#   a1[i]*=0.65
# print(sum(a1)-sum(a2), max(max(a1), max(a2)))

#------------10000-----------------------
# f = open('26_10000.txt')
# n, k = map(int, f.readline().split())
# disks = list(map(int, f.readline().split()))
# a = list(tuple(map(int, i.split())) for i in f)
# imp_files = sorted([i[0] for i in a if i[1]==2], reverse=True)
# def_files = sorted([i[0] for i in a if i[1]==1], reverse=True)
# c=0
# for d in range(k):
#   i=0
#   while(disks[d]>0 and i<len(imp_files)):
#     file = imp_files[i]
#     if(file<=disks[d]):
#       disks[d]-=file
#       imp_files.pop(i)
#     else:
#       i+=1
#   i=0
#   while(disks[d]>0 and i<len(def_files)):
#     file = def_files[i]
#     if(file<=disks[d]):
#       disks[d]-=file
#       c+=1
#       def_files.pop(i)
#     else:
#       i+=1
# print(c, max(disks))

#------------3377-----------------------
# f = open('26_3377.txt')
# n = int(f.readline())
# a = list(list(map(int, i.split())) for i in f)
# trees = [0]*100_000
# c=0
# min_r = 10**20
# max_s = 0
# rows = {}
# for i in range(n):
#   rows[a[i][0]] = rows.get(a[i][0], []) + [a[i][1]]

# for i in rows:
#   t=-2
#   x=0
#   r = sorted(rows[i])
#   j=0
#   for j in range(1,len(a)):
#     if r[i] -r[i-1]>2:
#       if r[i-1]-t>2:
#         t=r[i-1]+2
#         count+=1
#       else:
#         t=r[i-1]
#     else:
#       t=r[i-1]
#   c+=x
#   if(max_s<x):
#     max_s = x
#     min_r = i
# print(min_r, c)

# a[0].append(0)
# i = 1
# while(i<n):
#   j=i
#   x=0
#   if(a[i-1][0]!=a[i][0]):
#     x=0
#     i+=1
#   elif(a[i][1] - a[i-1][1] <= 2):
#     x=0
#     i+=2
#   elif(a[i][1] - a[i-1][1] in (3, 4)):
#     x=1
#     i+=2
#   else:
#     x=2
#     i+=2
#   a[j].append(x)
#   c+=x
# rows = {}
# for i in range(n):
#   rows[a[i][0]] = rows.get(a[i][0], 0) + a[i][2]
# for i in sorted(rows.keys()):
#   if(rows[i]>max_s):
#     max_s = rows[i]
#     min_r = i
# print(c, min_r)


# f = open('26_3377.txt')
# n = int(f.readline())
# d = list(list(map(int, i.split())) for i in f)
# rous_res = 10**20
# rows = {}
# for i in range(n):
#   rows[d[i][0]] = rows.get(d[i][0], []) + [d[i][1]]
# max_c=0
# c=0
# for j in sorted(rows.keys()):
#     t=-2
#     count=0
#     a= sorted(rows[j])+[100000]
#     for i in range(1,len(a)):
#         if a[i] -a[i-1]>2:
#             if a[i-1]-t>2:
#                 t=a[i-1]+2
#                 count+=1
#             else:
#                 t=a[i-1]
#         else:
#             t=a[i-1]
#     c+=count
#     if count>max_c:
#         max_c=count
#         rous_res=j
#     elif count==max_c:
#         rous_res=min(rous_res,j)
# print(c, rous_res)


#-----------------------------------
f = open('26.txt')
a = sorted(int(i) for i in f)
nums = {}
for i in a:
  nums[i] = nums.get(i,0)+1

sums = set([0])
# print(nums)

for i in nums.keys():
  for j in tuple(sums):
    k=0
    # print(i,j,k)
    while(k<nums[i]):
      k+=1
      sums.add(j+k)
s = sorted(sums)
x=s[1]
for i in range(2,len(s)):
  if(s[i]-s[i-1]>1):
    print(s[i-1],s[i])
    break
print(sum(s), sum(i for i in range(1,602)))