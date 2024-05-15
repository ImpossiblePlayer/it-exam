#1 X
# p, v = map(int, input().split())
# q, m = map(int, input().split())
# trees = [0]*(2*(max(m, v)+max(p, q))+3)
# l = len(trees)//2
# for i in range(l+p-v, l+q+m+2):
#   if(i in tuple(range(l+p-v, l+p+v+1)) or i in tuple(range(l+q-m, l+q+m+1))):
#     trees[i]=1
# for i in range(l+q-m, l+p+v+2):
#   if(i in tuple(range(l+p-v, l+p+v+1)) or i in tuple(range(l+q-m, l+q+m+1))):
#     trees[i]=1
# # trees[l+v]=1
# # trees[l+p]=1
# print(sum(trees))


#2 X
# g1, g2 = map(int, input().split(':')) 
# p1, p2 = map(int, input().split(':')) 
# t = int(input())
# f1=f2=0
# s1=p1+g1
# s2=p2+g2
# if(t==2):
#   f1=g1
#   f2=p2
# else:
#   f1=p1
#   f2=g2
# r = s2-s1
# if(r+s1>s2):
#   print(r)
# elif(t==1 and r+s1==s2 and r+f1>f2):
#   print(r)
# else:
#   print(r+1)


#5 X
# n, k, d = map(int, input().split())
# nums=[(n, 0)]
# for day in range(d):
#   for num in range(len(nums)):
#     for i in range(10):
#       t = nums[num][0]*10+i
#       if(t%k==0):
#         nums.append((t, 1))
#       else:
#         nums.append((t, 0))
#     nums = list(filter(lambda x: x[1]==1, nums))
#     if(len(nums)==0):
#       break
# print(nums[-1][0] if len(nums)>0 else -1)

#8 X
# l, x1, v1, x2, v2 = map(int(input().split()))

# road = [0]*l

# #9 X
# n = int(input())
# nums = list(map(int, input().split()))
# even = any(i%2==0 for i in nums)
# if not(even):
#    print('x'*(n-1))
# else:
#   first_odd = next(i for i in range(len(nums)) if nums[i]%2!=0)
#   print('x'*(first_odd-1) + '+'*(first_odd==1) + '+'*(first_odd==n-1) + 'x'*(n-first_odd-3))

# # 1 2 3 4 5 6 7


f=1
i=1
s=0
n=7
while(i<=n):
  f*=i
  s+=f
  i+=1
print(s)

# for x in range(100):
#   s = 2*x 
#   for _ in range(9):
#     s+=1
#     s*=2
#   if(s==18430):
#     print(x)
  
def Gauss (matrix: list[list]):
	n = len(matrix)
	matrix_  = matrix.copy()
	for k in range(n):
		for i in range(n):
			matrix_[k][i] = matrix_[k][i] / matrix[k][k]
		for i in range(k+1, n):
			K = matrix_[i][k] / matrix_[k][k]
			for j in range(n):
			  matrix_ [i][j] = matrix_[i][j] - K * matrix_[k][j]
		# for i in range(n):
		#   for j in range(n):
		#     matrix[i][j] = matrix_[i][j]
	
	return matrix_

def square(a, n):
	for row in a:
		yield row + [0] * (n - len(row))
	for _ in range(len(a), n):
		yield [0] * n

m = []
l = int(input('введите длину матрицы: '))
w = int(input('введите ширину матрицы: '))
for i in range(w):
	x = []
	for j in range(l):
		x.append(int(input(f'введите элемент {i},{j}')))
	m.append(x)
m1 = square(m)
print(*Gauss(m), sep='\n')
