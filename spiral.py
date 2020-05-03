import turtle

t = turtle.Turtle()
t.speed("fastest")

for i in range(0, 360):
  t.forward(0.1 + i/10)
  t.left(5)

# keep window open
turtle.Screen().mainloop()