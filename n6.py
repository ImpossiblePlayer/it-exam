# from turtle import *
# tracer(0)
# k=18 #масштаб
# lt(90)

# #-----------ЧЕРЕПАХА-------------------
# for _ in range(3):
#   down()
#   for _ in range(2):
#     fd(7*k)
#     rt(90)
#     fd(7*k)
#     rt(90)
#   up()
#   fd(6*k)
#   rt(90)
#   fd(6*k)
#   lt(90)




# #-----------ЦАПЛЯ-------------------
# # for _ in range(5):
# #   # следующие две строки ресуют полуокружность и поворачивают черепаху
# #   circle(4*k, 180)
# #   right(180)
# #   left(90) # тут уже поворачиваем туда, куда хотим пойти дальше


# # Расставляет точки в целочисленных координатах
# penup()
# for x in range(-20, 20):
#   for y in range(-20, 20):
#     goto(x*k, y*k)
#     dot(k//5, 'blue')

# done()


# Повтори 36 [Вперёд 1 Направо 36]
# Поднять хвост
# Вперёд 4 Направо 90
# Опустить хвост
# Повтори 8 [Вперёд 6 Направо 90]
from turtle import *
lt(90)
tracer(0)
k = 50
for _ in range(36):
  fd(1*k)
  rt(36)
penup()
fd(4*k)
rt(90)
pendown()
for _ in range(8):
  fd(6*k)
  rt(90)
penup()

for x in range(-20, 20):
  for y in range(-20, 20):
    goto(x*k, y*k)
    dot(2, 'blue')
done()