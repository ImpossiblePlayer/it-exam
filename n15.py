for a in range(-128, 128):
  if all( (x+y<=22) or (y<=x-6) or (y>=a) for x in range(1,128) for y in range(1,128) ):
    print(a)