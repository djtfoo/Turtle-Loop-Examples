import turtle

t = turtle.Turtle()
t.speed("fastest")

t.penup()
t.goto(0, 200)
t.pendown()

for n in range(0, 4):  # number of spiral loops
  for i in range(0, 72):    # iterations for drawing one circle
    t.forward(0.1 + i/10)
    t.left(5)

# keep window open
turtle.Screen().mainloop()