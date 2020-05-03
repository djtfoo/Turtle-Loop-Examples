import turtle

t = turtle.Turtle()
t.speed("fastest")

for n in range(0, 36):  # number of circles
  for i in range(0, 36):    # iterations for drawing one circle
    t.forward(3)
    t.left(10)
  t.forward(6)
  t.left(10)
  t.forward(6)

# keep window open
turtle.Screen().mainloop()