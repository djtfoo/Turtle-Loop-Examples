import turtle

t = turtle.Turtle()
t.speed("fastest")

for n in range(0, 5): # number of circles
  for i in range(0, 72):    # iterations per circle
    t.forward(5)  # length to draw by
    t.right(5)  # rotate by 5 degrees
  t.forward(10) # move to next circle

# keep window open
turtle.Screen().mainloop()