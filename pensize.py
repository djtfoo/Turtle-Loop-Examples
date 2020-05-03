import turtle

t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("red")

for i in range(0, 20):
  t.pensize(i)
  t.forward(5)

t.penup()
t.forward(50)

# keep window open
wn.mainloop()