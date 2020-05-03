import turtle

wn = turtle.Screen()
wn.bgcolor("white")

t = turtle.Turtle()
t.speed(10)

t.left(110)

fill_colors = ["orange", "purple", "blue", "red", "green", "yellow", "pink", "black"]

for i in range(0, len(fill_colors)):
  t.pencolor(fill_colors[i])
  t.fillcolor(fill_colors[i])
  t.begin_fill()
  for j in range(0, 4):
    t.forward(100)
    t.left(90)
  t.right(20)
  t.end_fill()

# keep window open
wn.mainloop()