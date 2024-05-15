# print(' ', 'y', ' ', 'z', '', 'f')
# for x in range(2):
#   for y in range(2):
#     for z in range(2):
#       for w in range(2):
#         f = (not(not x or z) or y) or not(w)
#         if(not(f)):
#           print(x, y, z, w, '', int(f))

from itertools import *
def f(x,y,w,z):
  return (x or not y) and not(x==z) and w

# for a1,a2,a3,a4,a5, a6 in product([0,1], repeat=6):
#   t=[(a1,a2,1,0),(a3,0,a4,1),(1,a5,0,a6)]
#   if len(t)==len(set(t)): # каждое значение встречается только один раз
#     for p in permutations('xywz'):
#       if [f(**dict(zip(p,r))) for r in t] == [1,1,1]:
#         print(p)

for a1, a2, a3, a4, a5, a6 in product([0,1], repeat=6):
  t=[(1,0,a1,a2),(0,1,1,a3),(a4,a5,0,a6)]
  if len(t)==len(set(t)):
    for p in permutations('xywz'):
      if [f(**dict(zip(p,r))) for r in t] == [1,1,1]:
        print(p)