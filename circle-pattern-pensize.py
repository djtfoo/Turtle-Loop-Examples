import turtle

t = turtle.Turtle()
t.speed("fastest")

for n in range(0, 36):  # number of circles
  pensize = 0
  for i in range(0, 72):    # iterations for drawing one circle
    pensize += 0.1
    t.pensize(pensize)
    t.forward(5)
    t.left(5)
  t.forward(10)
  t.left(10)
  t.forward(10)

# keep window open
turtle.Screen().mainloop()