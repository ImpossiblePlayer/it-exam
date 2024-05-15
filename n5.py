# m = 0
# for n in range(1, 1855663):
#   b = bin(n)[2:]
#   if(n%5==0):
#     b+='101'
#   else:
#     b+='1'
#   r=int(b, 2)
#   if(r%7==0):
#     b+='111'
#   else:
#     b+='1'
#   r = int(b, 2)
#   if(r<1855663):
#     m=n
# print(m)

# a=[]
# for n in range(10_000):
#   b=f'{n:b}'
#   b+=f'{n%4:b}'
#   r=int(b,2)
#   a+=[r]

# b=[0]*(max(a)+100)
# for r in a:
#   b[r]=1
# m=max(sum(b[i:i+49]) for i in range(len(b)-49))
# print(m)

#-----------12459-----------------------
# def change_notation(n, k):
#   r = ""
#   while(n>0):
#     r += str(n%k)
#     n//=k
  
#   return r[::-1]

# # for i in range(360+1):
# #   r = change_notation(i, 4)
# #   if((len(r)-r.count('0'))%2==0):
# #     r=r[:len(r)//2]+'0'+r[len(r)//2:]
# #   if(int(r)<=180):
# #     print(i, r)

# for i in range(2, 180):
#   r = oct(i)[2:]
#   if sum(int(j) for j in str(i))%2==0:
#     r+=str(i%3)
#   else:
#     r = max(c for c in r) + r
#   if(int(r)>127):
#     print(i, r)



# def change_not(n, k):
#   r=''
#   while(n>1):
#     r+=str(n%k)
#     n//=k
#   return r[::-1] if r else str(n)

# for i in range(2000):
#   r = change_not(i, 7)
#   if(sum(int(i) for i in r)%2==0):
#     r+='0'
#   else: r = '6'+r[1:]
#   x = int(r, 7)
#   if(x<119):
#     print(i, x)


def change(n, k):
  r = ''
  if(n in [0,1]):
    return str(n)
  while(n>0):
    r+=str(n%k)
    n//=k
  return r[::-1]

for i in range(2,1000):
  r = change(i, 3)
  c2 = r.count('2')
  r+=change(c2,3)
  c1 = r.count('1')
  r+=change(c1,3)
  c0 = r.count('0')
  r+=change(c0,3)
  if(int(r,3)<1000):
    print(i,int(r,3))