# file = open('17.txt')
# nums = [int(i) for i in file.read().strip().split()]
# min_num = min(i for i in nums if i%10==3 and 99<i<1000)

# count=0
# max_sum=0
# answer = []
# for i in range(len(nums)-1):
#   n1 = nums[i]
#   n2 = nums[i+1]
#   if (
#     (1000<=n1<=9999) + (1000<=n2<=9999)==1
#     and(n1**2 + n2**2)%min_num==0
#   ):
#     answer.append(n1**2 + n2**2)
# print(len(answer), max(answer))

#-----------4597-----------------------
# file = open('17.txt')
# nums = [int(i) for i in file.read().strip().split()]
# min_num = min(nums)
# count=0
# max_sum=0

# for i in range(len(nums)-1):
#   n1 = nums[i]
#   n2 = nums[i+1]
#   if(n1%117==min_num or n2%117==min_num):
#     count+=1
#     max_sum = max(max_sum, n1 + n2)
# print(count, max_sum)

#-----------12471-----------------------
# file = open('17.txt')
# nums = [int(i) for i in file.read().strip().split()]
# max_n = max(i for i in nums if i%100==13)
# ans = []
# c=0
# for i in range(len(nums)-2):
#   n1, n2, n3 = nums[i:i+3]
#   if (n1+n2+n3)<=max_n and (all(i%2==0 for i in [n1, n2, n3]) or any( (i>=10) and (i<100) for i in [n1, n2, n3])):
#     c+=1
#     ans.append(n1+n2+n3)
# print(c, sum(ans)//c)

#-----------яндекс-----------------------
f = open('17.txt')
a = [int(i) for i in f]
n = len(a)
c = 0
m = (max(i for i in a if i>=1000 and i<10000))**3
max_sum = 0
for i in range(2,n):
  x,y,z = a[i-2:i+1]
  if(sum(j%10==3 or j%10==5 for j in [x,y,z])>1 and x*y*z<=m):
    c+=1
    max_sum = max(max_sum, x+y+z)
print(c,max_sum)