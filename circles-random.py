import turtle
import random

t = turtle.Turtle()
t.speed("fastest")

for n in range(0, 5):   # number of circles
  for i in range(0, 72):
    r = random.random()
    t.forward(1 + r)
    t.left(5)

# keep window open
turtle.Screen().mainloop()