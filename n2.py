print(' ', 'y', ' ', 'z', '', 'f')
for x in range(2):
  for y in range(2):
    for z in range(2):
      for w in range(2):
        f = (not(not x or z) or y) or not(w)
        if(not(f)):
          print(x, y, z, w, '', int(f))