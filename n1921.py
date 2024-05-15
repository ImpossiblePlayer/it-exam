# для одной кучи
def f(s, m):
  if s>=165: return m%2==0
  if m==0: return 0
  h = [f(s+1, m-1), f(s*2, m-1)] # выполняем все возможные действия
  return any(h) if m%2!=0 else all(h) # возвращаем any когда ходим мы и all, когда ходит оппонент
                                          # (для  того, чтобы при любом ходе оппонента мы могли победить)

# print(19, [s for s in range(1, 165) if f(s, 1)])
# print(20, [s for s in range(1, 165) if not f(s, 1) and f(s, 3)])
# print(21, [s for s in range(1, 165) if not f(s, 2) and f(s, 4)])

# для двух куч
def f(a, b, m):
  if a+b>=288: return m%2==0
  if m==0: return 0
  h = [f(a+1, b, m-1), f(a*3, b, m-1), f(a+6, b, m-1), f(a, b*3, m-1), f(a, b+2, m-1), f(a, b+6, m-1)]
  return any(h) if m%2!=0 else all(h) # all -> any в 19
print(19, [s for s in range(1, 105) if f(4, s, 2)])
print(20, [s for s in range(1, 105) if not f(17, s, 1) and f(17, s, 3)])
print(21, [s for s in range(1, 105) if not f(4, s, 2) and f(4, s, 4)])


def win1(a, b):
  return min(a, b)+max(a, b)*3 >= 99

def win2(a, b):
  f = defeat(a+1, b) or defeat(a*3, b) or defeat(a, b+1) or defeat(a, b*3)
  h = not win1(a, b)
  return f and h

def defeat(a, b):
  f = win1(a+1, b) and win1(a*3, b) and win1(a, b+1) and win1(a, b*3)
  h = not win1(a, b)
  return f and h

def defeat2(a, b):
  f = (
    (win2(a+1, b) or win1(a+1, b)) and
    (win2(a*3, b) or win1(a*3, b)) and
    (win2(a, b+1) or win1(a, b+1)) and
    (win2(a, b*3) or win1(a, b*3))
  )
  h = not(win1(a+1, b) and win1(a, b+1) and win1(a*3, b) and win1(a, b*3))
  return f and h and not(win1(a, b))

# count = 0
# for i in range(8, 9):
#   for j in range(1, 91):
#     if defeat(i, j):
#       count+=1
#       print(i, j)
# print(count)


# import math
# def win1(a, b):
#   return a+b <= 18

# def defeat1(a, b):
#   f = win1(a-1, b) and win1(math.ceil(a/2), b) and win1(a, b-1) and win1(a, math.ceil(b/2))
#   h = not win1(a, b)
#   return f and h

# def win2(a, b):
#   f = defeat1(a-1, b) or defeat1(math.ceil(a/2), b) or defeat1(a, b-1) or defeat1(a, math.ceil(b/2))
#   h = not win1(a, b)
#   return f and h

# def defeat2(a, b):
#   f = (
#     (win2(a-1, b) or win1(a-1, b)) and
#     (win1(math.ceil(a/2), b) or win1(math.ceil(a/2), b)) and
#     (win2(a, b-1) or win1(a, b-1)) and
#     (win1(a, math.ceil(b/2)) or win1(a, math.ceil(b/2)))
#   )
#   h = not(win1(a+1, b) and win1(a, b+1) and win1(a+b, b) and win1(a, b+a))
#   return f and h and not(win1(a, b))

# count = 0
# for i in range(1, 100000):
#   if defeat1(i, i):
#     count+=1
#     print(i)

# print(count)
# print(defeat1(13, 13))