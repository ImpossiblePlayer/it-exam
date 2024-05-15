# for a in range(1, 128):
#   if all( ((x%2==0) <= (x%3!=0)) or (x+a>=80) for x in range(1,1024)):
#     print(a)

# c= list(range(29, 101))
# d= list(range(7, 69))
# for x in range(-1024, 1024):
#   c = 28<x<101
#   d = 6<x<69
#   if not (d<= (((not c) and (not 0)) <= (not d))):
#     print(x)


for a in range(120):
  if all((x&91 ==0) or ((x&77==0)<=(x&a!=0)) for x in range(500)):
    print(a)