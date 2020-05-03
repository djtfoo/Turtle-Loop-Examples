import turtle

t = turtle.Turtle()
t.speed("fastest")

for n in range(0, 36):
  t.forward(200)
  t.right(190)

# keep window open
turtle.Screen().mainloop()