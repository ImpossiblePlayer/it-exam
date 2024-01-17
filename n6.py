from turtle import *
tracer(0)
k=15 #масштаб

#-----------ЧЕРЕПАХА-------------------
# for _ in range(6):
#   forward(1*k)
#   right(90)
#   forward(7*k)




#-----------ЦАПЛЯ-------------------
for _ in range(5):
  # следующие две строки ресуют полуокружность и поворачивают черепаху
  circle(4*k, 180)
  right(180)
  left(90) # тут уже поворачиваем туда, куда хотим пойти дальше


# Расставляет точки в целочисленных координатах
penup()
for x in range(-20, 20):
  for y in range(-20, 20):
    goto(x*k, y*k)
    dot(3, 'blue')

done()