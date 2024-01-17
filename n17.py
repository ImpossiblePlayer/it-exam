file = open('17.txt')
nums = [int(i) for i in file.read().strip().split()]

min_num = min([i for i in nums if i%10==3 and 99<i<1000])


count=0
max_sum=0
answer = []
for i in range(len(nums)-1):
  n1 = nums[i]
  n2 = nums[i+1]
  if (
    (1000<=n1<=9999) + (1000<=n2<=9999)==1
    and(n1**2 + n2**2)%min_num==0
  ):
    answer.append(n1**2 + n2**2)

print(len(answer), max(answer))