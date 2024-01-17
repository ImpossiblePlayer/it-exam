values = []

# 1 
# for x in range(2):
#   for y in range(2):
#     for z in range(2):
#       for w in range(2):
#         if (x+y) and (y!=z) and not(w):
#           values.append([x, y, z, w])

# 2
# for a in range(2):
#   for b in range(2):
#     for c in range(2):
#       for d in range(2):
#         if ((a and b)==(not c))and(b<=d):
#           values.append([a, b, c, d])


# for x in range(2):
#   for y in range(2):
#     for z in range(2):
#       for w in range(2):
#         if (x or (y and not(z)) or w) == (x <= ((not(y)) or z)):
#           values.append([x, y, z, w])


for x in range(2):
  for y in range(2):
    for z in range(2):
        if ((x+y)<=(z==x))==False:
          values.append([x, y, z, ((x+y)<=(z==x))])




print(' x  y  z  F')
print(*values, sep='\n')