#-----------4605-----------------------
# f = open('27B.txt').readlines()
# n = int(f[0])
# k=36
# nums = list(tuple(map(int, i.split())) for i in f[1:])
# points = [i[0] for i in nums]
# p = [nums[i][1]//k if nums[i][1]%k==0 else nums[i][1]//k+1 for i in range(n)]
# boxes = [nums[0][1]//k if nums[0][1]%k==0 else nums[0][1]//k+1]

# for i in range(1, n):
#   boxes.append(boxes[i-1]+nums[i][1]//k if nums[i][1]%k==0 else nums[i][1]//k+1 + boxes[i-1])

# cost=0
# for i in range(n):
#   cost+=(points[i]-points[0])*p[i]
# m=cost
# for i in range(1, n):
#   delta = (2*boxes[i-1]-boxes[n-1])*(points[i]-points[i-1])
#   cost+=delta
#   m=min(m, cost)
# print(m)

#-----------7691-----------------------
# f = open('27B.txt').readlines()
# n, m = map(int, f[0].split())
# nums = [tuple(map(int, i.split())) for i in f[1:]]
# houses = [0]*(m+1)
# min_s = 10**100
# min_id=0
# for i in nums:
#   houses[i[0]] = i[1]
# people=[0]*(m+1)

# r=0
# for i in range(1, m+1):
#   r+=houses[i]*(i-1)
# for i in range(1, m+1):
#   people[i]=people[i-1]+houses[i]

# for i in range(1, m+1):
#   delta=2*people[i-1]-people[-1]
#   r+=delta
#   if(houses[i]==0 and min_s>=r):
#     min_s=r
#     min_id=i

# print(min_id)

#-----------8513-----------------------
# f = open('27B.txt').readlines()
# k = int(f[0])
# n = int(f[1])
# max_s=0
# nums = list(map(int, f[2:]))
# x=0
# for i in range(k, n):
#   x = max(x, nums[i-k])
#   max_s = max(max_s, x+nums[i])
# print(max_s)

#-----------11957-----------------------
# f = open('27B.txt').readlines()
# n, t, k = map(int, f[0].split())
# nums = list(tuple(map(int, i.split())) for i in f[1:])
# max_s=0
# min_x=10*100
# for i in range(t, n):
#   min_x = min(min_x, nums[i-t][0])
#   max_s = max(max_s, (nums[i][1]-min_x)*(k//min_x))
# print(max_s)

#-----------12934-----------------------
# f = open('27B.txt').readlines()
# k = int(f[0])
# n = int(f[1])
# nums = list(map(int, f[2:]))
# max_s=0
# s=0
# b = e = 0
# while(e<n):
#   while(s<=k and e<n):
#     s+=nums[e]
#     e+=1
#   max_s = max(max_s, e-b-1)
#   while(s>k and b<e):
#     s-=nums[b]
#     b+=1
# print(max_s)

#-----------7879-----------------------
# f = open('27A_7879.txt').readlines()
# n=int(f[0])
# k=int(f[1])
# nums=list(map(int, f[2:]))
# q=[nums[:k-1]]
# max_sum=0
# for i in range(k, n):

#-----------7627-----------------------
# f=open('27B.txt').readlines()
# k=int(f[0])
# n=int(f[1])
# nums=list(map(int, f[2:]))
# m=nums[0]
# max_num=0
# for i in range(k, n):
#   m=max(m, nums[i-k])
#   max_num=max(max_num, m+nums[i])
# print(max_num)

#-----------7627-----------------------
# f=open('27B.txt').readlines()
# n=int(f[0])
# houses=list(map(int, i.split()) for i in f[1:])
# k=44
# cost=0
# for i in houses:
#   cost+=i[0]*(i[1]//k + (i[1]%k))
# min_s=cost
# for i in houses:
#   delta=

#-----------6529-----------------------
# f=open('27B.txt').readlines()
# n, k = map(int, f[0].split())
# nums = list(map(int, f[1:]))
# max_s=0
# s=0
# b = e = 0
# while(e<n):
#   while(s<=k and e<n):
#     s+=nums[e]
#     e+=1
#   max_s = max(max_s, e-b-1)
#   while(s>k and b<e):
#     s-=nums[b]
#     b+=1
# print(max_s)

#-----------6638-----------------------
# f = open('27t.txt').readlines()
# n = int(f[0])
# k = 100
# nums = list(tuple(map(int, i.split())) for i in f[1:])
# points = [i[0] for i in nums]
# p = [nums[i][1]//k + (nums[i][1]%k!=0) for i in range(n)]
# boxes = [nums[0][1]//k + (nums[0][1]%k!=0)]
# for i in range(1, n):
#   boxes.append(boxes[i-1]+nums[i][1]//k + (nums[i][1]%k!=0))
# cost=0
# for i in range(n):
#   cost+=(points[i]-points[0])*p[i]
# # print(p)
# m=cost
# print(cost)
# m_id=0
# for i in range(1, n):
#   delta = (2*boxes[i-1]-boxes[n-1])*(points[i]-points[i-1])
#   cost+=delta
#   # print(cost, delta)
#   if(m>cost):
#     m=cost
#     m_id=nums[i][0]
# # print(nums)
# print(m_id)

#-----------7275-----------------------
# f = open('27_A_7275.txt').readlines()
# n, m = map(int, f[0].split())
# nums = list(list(map(int, i.split())) for i in f[1:])
# t=30
# # max_k=0
# for i in range(0, n):
#   nums[i][1]=nums[i][1]//t if nums[i][1]%t==0 else nums[i][1]//t +1

# # for i in range(n):
# #   t = nums[i][1]
# #   for j in range(n):
# #     if i!=j and abs(nums[i][0]-nums[j][0])<=m:
# #       t+=nums[j][1]
# #   max_k = max(max_k, t)
# # print(max_k)

# print(*nums)
# n1=nums[-1][0]
# road = [0]*(m+1) + [0]*n1 + [0]*m
# for i in range(n):
#   road[m+nums[i][0]]=nums[i][1]
# boxes=[road[0]]

# for i in range(1, len(road)):
#   boxes.append(boxes[i-1] + road[i])
# cm=0
# for i in range(m+1, m+2*n+1):
#   if(road[i]!=0):
#     c=boxes[i+m+1]-boxes[i-m-1]
#     cm=max(cm, c)
# print(cm)
# print(len(boxes), m)

#-----------6032-----------------------
# f = open('27_B_6032.txt').readlines()
# n=int(f[0])
# nums = list(list(map(int, i.split())) for i in f[1:])
# s=0
# t=13
# min_r=10**20
# for i in range(n):
#   s+=max(nums[i])
#   if(abs(nums[i][0]-nums[i][1])%t!=0):
#     min_r=min(min_r, abs(nums[i][0]-nums[i][1]))
# if(s%t==0):
#   s-=min_r
# print(s)


#-----------108-----------------------
# f = open('27-B_108.txt').readlines()
# n = int(f[0])
# nums = list(tuple(map(int, i.split())) for i in f[1:])
# s=0
# min_r=10**20
# for i in range(n):
#   s+=max(nums[i])
#   if(nums[i][1]!=nums[i][0]):
#     min_r=min(min_r, abs(nums[i][0]-nums[i][1]))
# if(s%5==0):
#   s-=min_r
# print(s)

#-----------6057-----------------------
# f = open('27_B_6057.txt').readlines()
# n = int(f[0])
# nums = list(tuple(map(int, i.split())) for i in f[1:])
# s=0
# min_r=10**20
# for i in range(n):
#   l = sorted(nums[i])
#   s+=l[-1]
#   if((l[-1]-l[1])%91!=0):
#     min_r=min(min_r, l[-1]-l[1])
#   elif((l[-1]-l[0])%91!=0):
#     min_r=min(min_r, l[-1]-l[0])
# if(s%91==0):
#   s-=min_r
# print(s)

#-----------637-----------------------
# f = open('27-B_637.txt').readlines()
# n = int(f[0])
# nums = list(tuple(map(int, i.split())) for i in f[1:])
# s=0
# min_r=10**20
# for i in range(n):
#   a, b = sorted(nums[i])
#   s+=b
#   if((b-a)%10!=0):
#     min_r=min(min_r, abs(b-a))
# if(s%10==5):
#   s-=min_r
# print(s)

#-----------890-----------------------
# f = open('27B_890.txt').readlines()
# n = int(f[0])
# nums = list(tuple(map(int, i.split())) for i in f[1:])
# max_s=0
# min_s=0
# r=[10**20]*10
# for i in range(n):
#   a, b = sorted(nums[i])
#   max_s+=b
#   min_s+=a
#   d=b-a
#   r[d%10]=min(r[d%10], d)
# print(min_s)
# if(max_s%10!=min_s%10):
#   min_s += r[(max_s-min_s)%10]
# print(min_s)

#-----------906-----------------------
# f=open('27-B_906.txt')
# n = int(f.readline())
# a=[0]*10
# x, y = map(int, f.readline().split())
# if x%10!=y%10:
#     a[x%10]=x
#     a[y%10]=y
# else:
#     a[x%10]=max(x,y)
# for i in range(1,n):
#     x, y = map(int, f.readline().split())
#     b=[0]*10
#     for j in range(10):
#         if a[j]!=0:
#             t=x+a[j]
#             b[t%10]=t
#     for j in range(10):
#         if a[j]!=0:
#             t=y+a[j]
#             b[t%10]=max(b[t%10],t)
#     a=b[:] # глубокое копирование
# print(a[8])

#-----------903-----------------------
# f = open('27-A_903.txt').readlines()
# n = int(f[0])
# nums = list(tuple(map(int, i.split())) for i in f[1:])
# s=0
# min_r=10**20
# for i in range(n):
#   a, b = sorted(nums[i])
#   s+=a
#   if((b-a)%3!=0):
#     min_r=min(min_r, abs(b-a))
# if(s%3==0):
#   s+=min_r
# print(s)

#-----------2257----------------------- ПОДПОСЛЕДОВАТЕЛЬНОСТЬ С КРАТНЫМ КОЛИЧЕСТВОМ ЭЛЕМЕНТОВ
# f = open('27t.txt')
# n = int(f.readline())
# s=0
# count=0
# ch=[0]*10
# max_s=0
# for i in range(n):
#   x = int(f.readline())
#   s+=x
#   if(x%5==0):
#     count+=1
#     if(ch[count%10]==0):
#       ch[count%10]=s
#   if count%10==0:
#     max_s=max(max_s, s)
#   elif(ch[count%10]!=0):
#     max_s=max(max_s, s-ch[count%10])
# print(max_s)

#-----------6323-----------------------
# f = open('27B_6323.txt').readlines()
# n, m = map(int, f[0].split())
# nums = list(tuple(map(int, i.split())) for i in f[1:])
# nums.sort()
# points_distance = [i[0] for i in nums]
# points_trips = [i[1]//m + (i[1]%m!=0) for i in nums]
# points_cost = [nums[0][0]]
# for i in range(1, n):
#   points_cost.append(points_cost[i-1]+points_trips[i])

# s = m = cost = sum((points_distance[i]-points_distance[0])*points_trips[i] for i in range(n))
# for i in range(1, n):
#   delta = (2*points_cost[i-1] - points_cost[n-1])*(points_distance[i] - points_distance[i-1])
#   cost+=delta
#   m=min(m, cost)
# print(m)

#-----------282----------------------- ОЧЕРЕДИ (ТУТ НЕ НУЖНЫ ОНИ)
# f = open('27-B_282.txt').readlines()
# n = int(f[0])
# nums = [int(i) for i in f[1:]]
# m = nums[0]
# s = 0
# for i in range(8, n):
#   m = max(m, nums[i-8])
#   s = max(s, m*nums[i])
# print(s)

#-----------3587----------------------- КОЛЬЦЕВАЯ ДОРОГА
# f = open('27_B_3587.txt').readlines()
# n = int(f[0])
# nums = [int(i) for i in f[1:n]] # надо считывать до n, потому что могут подсунуть лишнее число
# a = nums*3
# min_s = 10**20 
# id = 0
# # for i in range(n, n+n): #---- A
# #   s=0
# #   for j in range(i-n//2, i+n//2):
# #     s+=a[j]*abs(i-j)
# #   print(s)
# #   if(s<min_s):
# #     min_s = s
# #     id = i-n+1
# # print(id)

# points_s = [a[0]] #---- B
# for i in range(1, len(a)):
#   points_s.append(points_s[-1]+a[i])
# cost = 0
# for i in range(n//2, n+n//2):
#   cost+=a[i]*abs(n-i)
# for i in range(n+1, n+n):
#   delta = (2*points_s[i-1] - points_s[i-n//2-1] - points_s[i+n//2-1])
#   cost+=delta
#   if(cost<min_s):
#     min_s = cost
#     id = i-n+1
# print(id)

#-----------6528----------------------- КОЛЬЦЕВАЯ ДОРОГА
# f = open('27B_6528.txt')
# n, k, m = map(int, f.readline().split())
# t=20
# nums = [0]*k
# for i in range(n):
#   x, y = map(int, f.readline().split())
#   y = y//t + (y%t!=0)
#   nums[x-1] = y
# a = nums*3
# s_min = 10**20

# # for i in range(k, k+k): #---- A
# #   s = 0
# #   l=r=i
# #   for j in range(i-k//2, i+k//2):
# #     s += a[j]*abs(i-j)
# #   if(a[i]==0):
# #     while(a[l]==0):
# #       l-=1
# #     while(a[r]==0):
# #       r+=1
# #     if(r-i>=m and i-l>=m):
# #       s_min = min(s, s_min)
# # print(s_min)

# points_s = [a[0]] #---- B
# for i in range(1, len(a)):
#   points_s.append(points_s[-1]+a[i])
# cost = 0
# i = k
# while(a[i]!=0):
#   i+=1
# l=i-1
# r=i
# while(a[r]==0):
#   r+=1
# for j in range(i-k//2, i+k//2):
#   cost+=a[j]*abs(i-j)
# for j in range(i+1, k+k):
#   delta = (2*points_s[j-1] - points_s[j+k//2-1] - points_s[j-k//2-1])
#   cost+=delta
#   if(a[j]==0):
#     if(j-l>=m and r-j>=m):
#       s_min = min(cost, s_min)
#   else:
#     l=j
#     r=j+1
#     while(a[r]==0):
#       r+=1
# print(s_min)

#-----------907-----------------------
# f = open('27B_907.txt')
# n = int(f.readline())
# s = 0
# min_diff = 10**20
# for i in range(n):
#   a, b = sorted(map(int, f.readline().split()))
#   s+=b
#   if((b-a)%10!=0):
#     min_diff = min(min_diff, abs(b-a))
# if(s%10==5):
#   s-=min_diff
# print(s)

#-----------814-----------------------
# f = open('27-B_814.txt')
# n = int(f.readline())
# s = 0
# min_diff = 10**20
# for i in range(n):
#   a, b = sorted(map(int, f.readline().split()))
#   s+=a
#   if((b-a)%10!=0):
#     min_diff = min(min_diff, abs(b-a))
# if(s%5==0):
#   s+=min_diff
# print(s)

#-----------23-----------------------
# f = open('27-B_23.txt')
# n = int(f.readline())
# s = 0
# min_diff = 10**20
# for i in range(n):
#   a, b = sorted(map(int, f.readline().split()))
#   s+=b
#   if((b-a)%3!=0):
#     min_diff = min(min_diff, abs(b-a))
# if(s%3==0):
#   s-=min_diff
# print(s)

#-----------1233-----------------------
# f = open('27_B_1233.txt')
# n = int(f.readline())
# s = 0
# k = 101
# min_diff = 10**20
# for i in range(n):
#   a, b, c = sorted(map(int, f.readline().split()))
#   s+=c
#   if((c-b)%k!=0):
#     min_diff = min(min_diff, abs(c-b))
#   if((b-a)%k!=0):
#     min_diff = min(min_diff, abs(b-a))
# if(s%k==0):
#   s-=min_diff
# print(s)

#-----------908-----------------------
# f=open('27-B_908.txt')
# n = int(f.readline())
# a=[10**20]*16
# x, y = map(int, f.readline().split())
# if x%16!=y%16:
#   a[x%16]=x
#   a[y%16]=y
# else:
#   a[x%16]=min(x, y)
# for i in range(1,n):
#   x, y = map(int, f.readline().split())
#   b=[10**20]*16
#   for j in range(16):
#     if a[j]!=0:
#       t=x+a[j]
#       b[t%16]=t
#   for j in range(16):
#     if a[j]!=0:
#       t=y+a[j]
#       b[t%16]=min(b[t%16], t)
#   a=b[:] # глубокое копирование
# print(a[15])

#-----------4206----------------------- КОЛЬЦЕВАЯ ДОРОГА
f = open('27A_4206.txt').readlines()
n = int(f[0])
nums = [int(i) for i in f[1:]] # надо считывать до n+1, потому что могут подсунуть лишнее число
a = nums*3
min_s = 10**20 
# for i in range(n, n+n): #---- A
#   s=0
#   for j in range(i-n//2, i+n//2):
#     s+=a[j]*abs(i-j)
#   min_s = min(min_s, s)
# print(min_s*3)
points_s = [a[0]] #---- B
for i in range(1, len(a)):
  points_s.append(points_s[-1]+a[i])
cost = 0
for i in range(n//2, n+n//2):
  cost+=a[i]*abs(n-i)
for i in range(n+1, n+n):
  delta = (2*points_s[i-1] - points_s[i-n//2-1] - points_s[i+n//2-1])
  cost+=delta
  if(cost<min_s):
    min_s = cost
print(min_s*3)

#-----------2256-----------------------
# f = open('27B_2256.txt')
# n = int(f.readline())
# s=0
# count=0
# t=3
# ch=[0]*t
# max_s=0
# for i in range(n):
#   x = int(f.readline())
#   s+=x
#   if(x%5==0):
#     count+=1
#     if(ch[count%t]==0):
#       ch[count%t]=s
#   if count%t==0:
#     max_s=max(max_s, s)
#   elif(ch[count%t]!=0):
#     max_s=max(max_s, s-ch[count%t])
# print(max_s)

#-----------3231-----------------------
# f = open('27-B_3231.txt').readlines()
# n = int(f[0])
# nums = [int(i) for i in f[1:n]] # надо считывать до n, потому что могут подсунуть лишнее число
# a=nums*3
# min_s = 10**20
# min_id = 0
# points_s = [a[0]]
# for i in range(1, len(a)):
#   points_s.append(points_s[-1]+a[i])
# cost=0
# for i in range(n//2, n+n//2):
#   cost+=a[i]*abs(n-i)
# for i in range(n+1, 2*n):
#   delta= (2*points_s[i-1] - points_s[i-n//2-1] - points_s[i+n//2-1])
#   cost+=delta
#   if(cost<min_s):
#     min_id=i-n+1
#     min_s = cost
# print(min_id)

#-----------6321-----------------------
# f = open('27A_6321.txt').readlines()
# n, v, m = map(int, f[0].split())
# nums = [tuple(map(int, i.split())) for i in f[1:]]
# nums.sort()
# boxes = [i[1]//v + (i[1]%v!=0) for i in nums]

# s = boxes[0]

# b=e=0
# while(nums[e+1][0] - nums[0][0] <= m):
#   e+=1
#   s+=boxes[e]
# max_s=s
# for i in range(1, n):
#   while(e+1!=n-1 and nums[e+1][0] - nums[i][0] <= m):
#     e+=1
#     s+=boxes[e]
#   while(nums[i][0] - nums[b][0] > m):
#     s-=boxes[b]
#     b+=1
#   max_s=max(max_s, s)
# print(max_s)

#-----------955-----------------------
# f=open('27B_955.txt')
# n = int(f.readline())
# a=[10**20]*256
# x, y = map(int, f.readline().split())
# if x%256!=y%256:
#   a[x%256]=x
#   a[y%256]=y
# else:
#   a[x%256]=min(x, y)
# for i in range(1,n):
#   x, y = map(int, f.readline().split())
#   b=[10**20]*256
#   for j in range(256):
#     if a[j]!=0:
#       t=x+a[j]
#       b[t%256]=t
#   for j in range(256):
#     if a[j]!=0:
#       t=y+a[j]
#       b[t%256]=min(b[t%256], t)
#   a=b[:] # глубокое копирование
# print(a[31])

#-----------69-----------------------
# f=open('27B_69.txt').readlines()
# n=int(f[0])
# nums = [int(i) for i in f[1:n+1]]
# # for i in range(n): #---- A
# #   for j in range(i+1, n):
# #     if abs(nums[i]-nums[j])%13==0 and nums[i]*nums[j]%2==0:
# #       c+=1
# c=0
# diff=[[0]*13, [0]*13]
# for i in range(n):
#   if(nums[i]%2==0):
#     c+=diff[0][nums[i]%13]
#     c+=diff[1][nums[i]%13]
#   else:
#     c+=diff[0][nums[i]%13]
#   diff[nums[i]%2][nums[i]%13]+=1
# print(c)

#-----------317-----------------------
# f = open('27-B_317.txt').readlines()
# n = int(f[0])
# nums = [int(i) for i in f[1:n+1]]
# d = [0]*34
# c=0
# # for i in range(n-1):
# #   for j in range(i+1, n):
# #     if(nums[j] < nums[i]) and nums[i]+nums[j]<=34:
# #       c+=1
# for j in range(n):
#   if(nums[j]<17):
#     c+=sum(d[nums[j]+1:34-nums[j]+1])
#   if(nums[j]<34):
#     d[nums[j]]+=1
# print(c)

#-----------508----------------------- УНИКАЛЬНЫЕ ЧЕТВЕРКИ
# f = open('27-B_508.txt').readlines()
# n=int(f[0])
# nums = [int(i) for i in f[1:]]
# a = [0]*101
# c=0
# for i in range(n):
#   a[nums[i]]+=1
# even=odd=odd_pairs=even_pairs=0
# for i in range(1, 101):
#   if(a[i]>=2):
#     if(i%2==0):
#       even_pairs+=1
#     else:
#       odd_pairs+=1
#   if(a[i]>=1):
#     if(i%2==0):
#       even+=1
#     else:
#       odd+=1
# c=odd_pairs*even_pairs
# c+=odd_pairs*(even**2-even)//2
# c+=even_pairs*(odd**2-odd)//2
# c+=((even**2-even)//2)*((odd**2-odd)//2)
# print(c)

#-----------442-----------------------
# f = open('27-B_442.txt').readlines()
# n = int(f[0])
# nums = [int(i) for i in f[1:n+1]]
# c=0
# # for i in range(n-1):
# #   r=False
# #   for j in range(i+1, n):
# #     if(nums[j]==0):
# #       r=True
# #     elif(r and nums[i]!=0 and (nums[i]+nums[j])%2==0):
# #       c+=1
# #       print(nums[i], nums[j], c)
# k0=[0, 0]
# k=[0, 0]
# for i in range(n):
#   if(nums[i]==0):
#     k0[0]+=k[0]
#     k0[1]+=k[1]
#     k = [0, 0]
#   else:
#     k[nums[i]%2]+=1
#     c+=k0[nums[i]%2]
# print(c)

#-----------682-----------------------
# f = open('27t.txt').readlines()
# n = int(f[0])
# nums = [tuple(map(int, i.split())) for i in f[1:n+1]]
# min_r=10**20
# for i in

# #-----------13622-----------------------
# f = open('27B_13622.txt').readlines()
# k = int(f[0])
# n = int(f[1])
# nums = sorted(int(i) for i in f[2:])
# c=0
# b=0
# e=n-1
# while(b<e):
#   while(b<e and nums[b]+nums[e]<=k):
#     b+=1
#   if(nums[b]+nums[e]>k and b<e):
#     c+=1
#   b+=1
#   e-=1
# print(c*2)

#-----------12479-----------------------
# f = open('27-A_12479.txt').readlines()
# k = int(f[0])
# n = int(f[1])
# nums = list(int(i) for i in f[2:])
# max_s=0
# ans = -10**20
# for i in range(k, n):
#   max_s = max(max_s, nums[i-k] - (i-k))
#   ans = max(ans, max_s + nums[i] + i)
# print(ans)
#-----------14405-----------------------
# f = open('27B_14405.txt').readlines()
# n, k = map(int, f[0].split())
# nums = list(map(int, f[1:n+1]))
# diff = [[0]*7, [0]*7, [0]*7, [0]*7, [0]*7, [0]*7]
# max_s = 0
# for i in range(k*6, n):
#   diff[0][nums[i-k*6]%7] = max(nums[i-k*6], diff[0][nums[i-k*6]%7])
#   for j in range(1, 6):
#     x = nums[i-k*(6-j)]
#     for z in range(7):
#       if(diff[j-1][z]!=0):
#         y = x + diff[j-1][z]
#         diff[j][y%7] = max(diff[j][y%7], y)
#   max_s = max(max_s, diff[5][(7-nums[i]%7)%7] + nums[i])
# print(max_s)

#-----------11604-----------------------
# def fn(n):
#   return bin(int(n))[2:].count('1')
# f = open('27B_11604.txt').readlines()
# k, n = map(int, f[:2])
# nums = list(map(fn, f[2:n+2]))
# diff = [[0]*21, [0]*21, [0]*21, [0]*21, [0]*21]
# for i in range(k*4, n):
#   diff[0][nums[i-k*4]]+=1
#   for j in range(1, 5):
#     x = nums[i-k*(5 - j-1)]
#     diff[j][x] += diff[j-1][x]
# print(sum(diff[4])%(2**61-1))

#-----------11673-----------------------
# f = open('27B_11673.txt').readlines()
# k, n = map(int, f[:2])
# a = list(map(int, f[2:n+2]))
# i, j = 1, 0
# c=0
# while(a[i]-a[j]<=k):
#   i+=1
# for z in range(i, n):
#   while(a[z]-a[j]>k):
#     j+=1
#   c+=j
# print(c*2)

#-----------11485-----------------------
# f = open('27-B_11485.txt').readlines()
# n = int(f[0])
# a = sorted(int(i) for i in f[1:n+1])
# b = sorted(int(i) for i in f[n+1:2*n+1])
# min_r = 10**20
# i, j = 0, 0
# for i in range(n):
#   while(j<n and a[j]<b[i]):
#     j+=1
#   min_r = min(min_r, abs(a[j-1]-b[i]))
#   if(j<n):
#     min_r = min(min_r, abs(a[j]-b[i]))
# print(min_r)
  
#-----------10134-----------------------
# k, n, *a = map(int, open('27A_10134.txt'))
# m0 = (10**50, -10**50)
# mp = (10**50, -10**50)
# mx = -10**50

# for i in range(2*k, n):
#     m0 = (min(m0[0], a[i-2*k]), max(m0[1], a[i-2*k]))

#     # так как при произведении знак может меняться
#     # проверим все комбинации произведений
#     mp = (min(mp[0], m0[0] * a[i-k], m0[1] * a[i-k]),
#           max(mp[1], m0[0] * a[i-k], m0[1] * a[i-k]))
#     mx = max(mx, mp[0] * a[i], mp[1] * a[i])
# print(mx % (10**9 + 7))

#-----------910-----------------------
# f = open('27-B_910.txt').readlines()
# n = int(f[0])
# nums = list(sorted(map(int, i.split())) for i in f[1:])
# min_r=10**10
# c=0
# s3=0
# for i in range(n):
#   a1, a2, a3 = nums[i]
#   s3+=a3
#   if((a3-a2)%2!=0):
#     min_r = min(min_r, a3-a2)
#   if((a3-a1)%2!=0):
#     min_r = min(min_r, a3-a1)
#   c+= 1 if a1%2!=a2%2 else 0

# if(c%2==0):
#   s3-=min_r
# print(s3, min_r, c)

#-----------937-----------------------
# f = open('27-A_937.txt')
# n=int(f.readline())
# s = 0
# c1=c0=c01=0
# min_r = 10**10
# for i in range(n):
#   a1, a2, a3 = sorted(map(int, f.readline().split()))
#   s+=a3
#   if(a3-a2)%2!=0:
#     min_r=min(min_r, a3-a2)
#   if(a3-a1)%2!=0:
#     min_r=min(min_r, a3-a1)
# print(s-min_r)

#-----------477-----------------------
# f = open('27-B_477.txt').readlines()
# n = int(f[0])
# nums = list(int(i) for i in f[1:])
# min_s = [10**10, 10**10]
# c = [0, 0]
# count=0
# for i in range(n):
#   if( nums[i]> min_s[abs(nums[i]%2-1)] ):
#     count+=c[abs(nums[i]%2-1)]
#   c[nums[i]%2]+=1
#   min_s[nums[i]%2] = min(min_s[nums[i]%2], nums[i])
# print(count)

#-----------10727-----------------------
# f = open('27-B_10727.txt').readlines()
# n = int(f[0])
# a = list(map(int,f[1:]))
# c1=c=count=0
# # словарь сразницами количества  четных и нечетных
# r = {}
# for i in range(n):
#   t=t1=0
#   if a[i]>0:
#     c+=1
#   elif a[i]<0:
#     c1+=1
#   if(c==c1):
#     count+=1
#   if(c-c1 in r):
#     count+=r[c-c1]
#   r[c-c1] = r.get(c-c1, 0) + 1
# print(count)

#-----------912-----------------------
# from itertools import product
# f = open('27A.txt').readlines()
# n=int(f[0])
# nums = list(tuple(map(int, i.split())) for i in f[1:])
# sums = tuple(map(sum, product(nums)))
# min_s = min(sums)
# print(max(i for i in sums if i%7==min_s%7))



#-----------9963-----------------------
# def delit(n):
#   a={}
#   i=2
#   while n>1:
#     while n%i==0:
#       a[i]=a.get(i,0)+1
#       n//=i
#     i+=1
#   return a

# f = open('27A_9963.txt').readlines()
# n=int(f[0])
# k=int(f[1])
# a = list(int(i) for i in f[2:])
# c=0
# b=0
# e=0
# nums_d = []
# d = {}
# for e in range(n):
#   nums_d.append(delit(a[e]))
#   c+=1
#   for i in nums_d[-1]:
#     d[i] = d.get(i, 0) + nums_d[-1][i]
#   if(len(d)<=k):
#     c+=e-b
#   else:
#     while(len(d)>k):
#       for i in nums_d[b]:
#         d[i]-= nums_d[b][i]
#         if(d[i]==0):
#           del d[i]
#       b+=1
#     c+=e-b
# print(c)

#-----------9848-----------------------
# f = open('27_B_9848.txt').readlines()
# k, n = map(int, f[:2])
# a = list(map(int, f[2:]))
# min_n = 10**20
# max_s = sum(a[:k+1])
# sums = [a[0]]
# for i in range(1, k+1):
#   sums.append(sums[i-1] + a[i])
  
# for i in range(k+1, n):
#   min_n = min(min_n, sums[i-k-1])
#   sums.append(sums[i-1] + a[i])
#   max_s = max(max_s, sums[i], sums[i]-min_n)
# print(max_s)

#-----------2904-----------------------
# f = open('27B_2904.txt').readlines()
# n = int(f[0])
# a = list(map(int, f[1:]))
# ids = [0]*2077
# ost = [10**20]*2077
# s = a[0]
# r=0
# min_s = 10**20
# ost[s%2077] = s
# for i in range(1, n):
#   s +=a[i]
#   if(s%2077==0):
#     if(s<min_s):
#       min_s =s
#       r=i+1
#   if(ost[s%2077]!=10**20):
#     if(s-ost[s%2077]<min_s):
#       min_s = s-ost[s%2077]
#       r=i-ids[s%2077]
#     elif(s-ost[s%2077]==min_s):
#       r = max(r, i-ids[s%2077])
#   if(ost[s%2077] == 10**20 or ost[s%2077] > s):
#     ost[s%2077] = s
#     ids[s%2077] = i
# print(r)

#-----------2257-----------------------
# f = open("27A.txt")
# n = int(f.readline())
# s = 0
# even = [0] + [100000000000000] * 9
# count_even = 0
# ans = -100000000000000
# for i in range(n):
#     x = int(f.readline())
#     count_even += (x % 2 == 0)
#     s += x
#     ost = count_even % 10
#     if s - even[ost] > ans:
#         ans = s - even[ost]
#     if s < even[ost]:
#         even[ost] = s
# print(ans)

#-----------4116-----------------------
# f = open('27.txt')
# n, k = map(int, f.readline().split())
# nums = [int(i) for i in f]
# # max_c = 0
# # for i in range(n):
# #   c0=s=0
# #   for j in range(i, n):
# #     s+=nums[j]
# #     c0+=1
# #     if s<=k:
# #       max_c= max(max_c, c0)
# #     else: break

# s = nums[0]
# b = e = 0
# while s+nums[e+1]<=k:
#   s+=nums[e+1]
#   e+=1
# max_c = e-b+1
# while(e<n):
#   s-=nums[b]
#   b+=1
#   while(e<n and s + nums[e+1]<=k):
#     s+=nums[e+1]
#     e+=1
#   max_c = max(max_c, e-b+1)
# print(max_c)

#-----------2903-----------------------
# f = open('27_2903.txt')
# n = int(f.readline())
# max_s = 10**20
# m = [0]*n
# s=c=0
# for i in range(n):
#   x=int(f.readline())
#   s+=x
#   if x%3==0:
#     c+=1
#   if c==10:
#     max_s = min(max_s, s)
#   if c>=10: 
#     max_s = min(max_s, s-m[s%10])
#   m[c]= max(m[c], s)
# print(max_s)

#-----------13102-----------------------
# f = open('27-B_13102.txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(f.readline()) for _ in range(n)]
# k*=2
# max_p = [-10**20, 0, 0]
# max_ = -10**20
# for i in range(k, n):
#   if(a[i]+a[i-k]>max_p[0]):
#     max_p = [a[i]+a[i-k], i-k, i]
# for i in range(n):
#   if(i not in max_p[1:] and a[i]>max_):
#     max_ = a[i]
# print(max_+max_p[0])

#-----------12114----------------------- ТРОЙКИ ЧИСЕЛ
# f = open('27B_12114.txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(f.readline()) for _ in range(n)]
# max1=a[0]
# maxs2 = max1+a[k]
# maxs3 = maxs2 + a[2*k]
# for i in range(2*k+1, n):
#   max1 = max(max1, a[i-2*k])
#   maxs2 = max(maxs2, max1 + a[i-k])
#   maxs3 = max(maxs3, maxs2+a[i])
# print(maxs3)

#-----------2363-----------------------
# f = open('27B_2363.txt')
# n = int(f.readline())
# k = 117
# a = [int(f.readline()) for _ in range(n)]
# t = [0]*k
# b=0
# e=4
# c=0
# sums=[a[0]]
# for i in range(1, n):
#   sums.append(sums[i-1] + a[i])
# ost = [0]*k

# for i in range(5, n):
#   if sums[i]%k==0:
#     c+=1
#   c+= ost[sums[i]%k]
#   ost[sums[i-5]%k]+=1
# print(c)

#-----------1764-----------------------
# f = open('27B_1764.txt')
# n = int(f.readline())
# a = [tuple(map(int, i.split())) for i in f]
# ost1 = [0]*5
# ost2 = [0]*5
# ost1[abs(a[0][0]-a[0][1])%5] = abs(a[0][0]-a[0][1])
# ost2[abs(a[0][0]-a[0][1])%5] = -abs(a[0][0]-a[0][1])
# r = 0
# for i in range(1, n):
#   r_t = abs(a[i][0] - a[i][1])
#   ost_t1 = [0]*5
#   ost_t2 = [0]*5
#   for j in range(5):
#     if(ost1[j]!=0):
#       sr = r_t + ost1[j]
#       if(sr<0):
#         ost_t2[abs(sr)%5] = sr
#       else:
#         ost_t1[sr%5] = sr
#   for j in range(5):
#     if(ost1[j]!=0):
#       sr = r_t - ost1[j]
#       if(sr<0):
#         ost_t2[abs(sr)%5] = min(ost_t2[abs(sr)%5], sr)
#       else:
#         ost_t1[sr%5] = max(ost_t1[sr%5], sr)
#   for j in range(5):
#     if(ost1[j]!=0):
#       sr = r_t + ost2[j]
#       if(sr<0):
#         ost_t2[abs(sr)%5] = min(ost_t2[abs(sr)%5], sr)
#       else:
#         ost_t1[sr%5] = max(ost_t1[sr%5], sr)
#   for j in range(5):
#     if(ost1[j]!=0):
#       sr = r_t - ost2[j]
#       if(sr<0):
#         ost_t2[abs(sr)%5] = min(ost_t2[abs(sr)%5], sr)
#       else:
#         ost_t1[sr%5] = max(ost_t1[sr%5], sr)
#   ost1 = ost_t1.copy()
#   ost2 = ost_t2.copy()
# print(max(ost1[0], abs(ost2[0])))


#-----------3295-----------------------
# f = open('27-B_3295.txt')
# n = int(f.readline().strip())
# a = [int(i.strip()) for i in f]
# nums = [21, 42, 63, 84]
# ids = {
#   441: -1, 1764: -1, 3969: -1, 7056: -1
# }
# pairs = []
# i=1
# while (i*21)**2 <= 10_000:
#   nums.append((i*21))
#   i+=1
# for i in range(n):
#   if(a[i] in nums and ids[a[i]**2]!=-1):
#     pairs.append(i-ids[a[i]**2]+1)
#   if(a[i] in ids.keys() and ids[a[i]]==-1):
#     ids[a[i]] = i

# print(max(pairs))

#-----------3768-----------------------
# f = open('27-B_3768.txt')
# n = int(f.readline())
# a = [int(i) for i in f]
# # def delit(n):
# #   d= {}
# #   i=2
# #   while(n>1):
# #     if(n%i==0):
# #       d[i] = d.get(i, 0) + 1
# #       n//=i
# #     else: i+=1
# #   return d
# # d = delit(8_023_320) # {2: 3, 3: 3, 5: 1, 17: 1, 19: 1, 23: 1}
# # nums_del = [delit(a[i]) for i in range(n)]
# t = 8_023_320
# r = 1

# del_t = {2: 0, 3: 0, 5: 0, 17: 0, 19: 0, 23: 0}
# m_b = b = 0
# length = 0
# # for i in range(n):
# #   x = nums_del[i]
# #   if any(k not in d.keys() for k in x.keys()):
# #     del_t = {2: 0, 3: 0, 5: 0, 17: 0, 19: 0, 23: 0}
# #     continue
# #   for k in x.keys():
# #     del_t[k] += x[k]
# #   if(any(del_t[k] > d[k] for k in del_t.keys())):
# #     while(any(del_t[k] > d[k] for k in del_t.keys())):
# #       for j in nums_del[d].keys():
# #         del_t[j]-=nums_del[d][j]
# for i in range(n):
#   if t%a[i]==0:
#     r*=a[i]
#     while(t%r!=0):
#       r//=a[b]
#       b+=1
#     if(length < i-b+1):
#       length = i-b+1
#       m_b = b
#   else:
#     b=i+1
#     r = 1
# print(m_b+1)

#-----------9992-----------------------
# f = open('27B_9992.txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(f.readline()) for _ in range(n)]
# a1 = a[0]
# a2 = a1+a[k]
# a3 = a2 + a[2*k]
# c=0
# if(a1*a2*a3==171 and sum(a1, a2, a3)%27==0):
#   c+=1
# for i in range(2*k+1, n):
#   if(a[i-2*k]*a2*a3==171 and sum(a[i-2*k], a2, a3)%27==0):
#     c+=1
#     a1 = a[i-2*k]
#   elif(a[i-k]*a1*a3==171 and sum(a[i-k], a1, a3)%27==0):
#     c+=1
#     a2 = a[i-k]
#   elif(a[i]*a2*a1==171 and sum(a[i], a2, a1)%27==0):
#     c+=1
#     a3 = a[i]
#   elif(a[i-2*k]*a[i-k]*a3==171 and sum(a[i-2*k], a[i-k], a3)%27==0):
#     c+=1
#     a1 = a[i-2*k]
#     a2 = a[i-k]
#   elif(a[i-2*k]*a2*a[i]==171 and sum(a[i-2*k], a2, a[i])%27==0):
#     c+=1
#     a1 = a[i-2*k]
#     a3 = a[i]
#   elif(a[i-k]*a1*a[i]==171 and sum(a[i-k], a2, a[i])%27==0):
#     c+=1
#     a2 = a[i-k]
#     a3 = a[i]
# print(c)








#-----------14960-----------------------
# f = open('27_B_14960.txt')
# n = int(f.readline())
# a = [int(i) for i in f]
# diffs = []
# for i in range(1, n):
#   diffs.append(a[i]-a[i-1])
# sums = [0]
# len_ = 0
# s = 0
# max_s = 0
# min_l = 10**20
# # print(diffs)
# for i in range(n-1):
#   s+=diffs[i]
#   len_+=1
#   if(s<=0):
#     s=0
#     len_=0
#   else:
#     if(s>max_s):
#       min_len = len_
#       max_s = s
#     elif(max_s==s):
#       min_len = len_
# print(max_s,  min_len+1)


#-----------12331-----------------------
# f = open('27B_12331.txt')
# n = int(f.readline())
# t = int(f.readline())
# a = [int(i) for i in f]

# ids = [[] for i in range(10)]
# uk = [0]*10
# K = []

# for i in range(t):
#   ids[a[i]].append(i)
# # print(a)
# for i in range(n):
#   if(i+t<n):
#     ids[a[i+t]].append(i+t)
#   k = 0
#   for j in range(1, 10):
#     if(ids[j]):
#       if (uk[j]<len(ids[j])) and (i-ids[j][uk[j]]<=t):
#         k=max(k, j*(i-ids[j][uk[j]]))
#       else:
#         uk[j]+=1
#         if(uk[j]<len(ids[j])):
#           k=max(k, j*(i-ids[j][uk[j]]))
#       if(ids[j][-1] - i <=t):
#         k=max(k, j*(ids[j][-1] - i))
#   K.append(k)
# print(sum(K))

#-----------10077-----------------------
# f = open('27B_10077.txt')
# n = int(f.readline())
# k = int(f.readline())
# a = [int(f.readline()) for _ in range(n)]
# S = sum(a)
# ost = [-1]*k

# max_len = 0
# id = 0
# s_t = 0
# for i in range(n):
#   s_t = s_t+a[i]
#   if(S - s_t)%k==0 and i!=n-1:
#     max_len = max(max_len, i+1)
#   else:
#     x = (s_t%k - S%k)%k
#     # print('x=',x)
#     if(ost[x]!=-1):
#       max_len = max(max_len, i-ost[x])
#       # print('max_len=',max_len)

#   ost[s_t%k] = i if ost[s_t%k]==-1 else ost[s_t%k]
#   # print(ost)
# print(max_len)

#-----------11244-----------------------
# f = open('27_B_11244.txt')
# k = int(f.readline())
# n = int(f.readline())
# a = [int(f.readline()) for _ in range(n)]

# max_ = [0]*k
# min_ = [0]*k
# max_num = -10**100
# for i in range(k):
#   max_[i%k] = a[i]
#   min_[i%k] = a[i]

# for i in range(k, n):
#   max_num = max(max_num, max_[i%k]*a[i], min_[i%k]*a[i])
#   max_[i%k]= max(a[i], max_[i%k])
#   min_[i%k]= min(a[i], min_[i%k])
# print(max_num)

#-----------10033-----------------------
f = open('27B_10033.txt')
n, w, k = map(int, f.readline().split())
gold = []
silver = []
for i in range(n):
  x, y = map(int, f.readline().split())
  if(y==0 and x<=k):
    silver.append(x)
  if(y==1 and x<=w):
    gold.append(x)
# A
# ans = [gold[0]]
# k_t = k
# w_t = w

# for i in range(1,len(gold)):
#   b = ans.copy()
#   for j in range(len(ans)):
#     if(gold[i]+ans[j]<=w):
#       b.append(gold[i]+ans[j])
#   b.append(gold[i])
#   ans = b[:]

# ans2 = [silver[0]]
# for i in range(1,len(silver)):
#   b = ans2.copy()
#   for j in range(len(ans2)):
#     if(silver[i]+ans2[j]<=k):
#       b.append(silver[i]+ans2[j])
#   b.append(silver[i])
#   ans2 = b[:]
# count=ans.count(w)
# for i in range(1, k+1):
#   count+=ans2.count(i)*ans.count(w-i)
# print(count)

# B
# ans = [0]*(w+1)
# ans2 = [0]*(k+1)

# for i in range(len(gold)):
#   for j in range(w-gold[i], 0, -1):
#     ans[j+gold[i]]+=ans[j]
#   ans[gold[i]]+=1
# for i in range(len(silver)):
#   for j in range(k-silver[i], 0, -1):
#     ans2[j+silver[i]]+=ans2[j]
#   ans2[silver[i]]+=1
# c=ans[w]
# for i in range(1, k+1):
#   c+=ans2[i]*ans[w-i]
# print(c%(10**9+7))


c=0
for k in range(-170, -101):
  for n in range(-189, -110):
    x1 = (5+10*k)/45
    x21 = (-3+9*n)/45
    x22 = (3+9*n)/45
    if(x1==x21 or x1==x22):
      print(x1)
      c+=1
print(c)