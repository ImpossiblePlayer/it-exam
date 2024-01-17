# chars = 'АВЕСТ'
# count = 1


# for i in chars:
#   for j in chars:
#     for k in chars:
#       for v in chars:
#         for w in chars:
#           word = i+j+k+v+w
#           if(word=='СВЕТА'):
#             print(count)
#           count+=1


count=0
for a in '012345678': 
  for b in '012345678':
    for c in '012345678':
      for d in '012345678':
        for e in '012345678':
          r = a+b+c+d+e
          if( r[0] not in '01357' and r[-1] not in '18' and r.count('3')<2 ):
            count+=1
print(count)