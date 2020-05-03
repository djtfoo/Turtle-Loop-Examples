import turtle

t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("red")

pensize = 1
for i in range(0, 120):
  pensize += 0.5
  t.pensize(pensize)
  if i % 20 == 0:
    pensize = 1
  t.forward(3)
  t.left(3)

# keep window open
turtle.Screen().mainloop()