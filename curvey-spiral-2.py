import turtle

t = turtle.Turtle()
t.speed("fastest")

for i in range(0, 720):
  t.forward(0.5 + (int)(i/100))
  t.left(5)

# keep window open
turtle.Screen().mainloop()