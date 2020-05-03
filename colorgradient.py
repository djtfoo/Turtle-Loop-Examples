import turtle

t = turtle.Turtle()
t.speed("fastest")
t.penup()
t.goto(-100, 200)
t.pendown()

color_r = 0
color_g = 0
color_b = 0
turtle.Screen().colormode(255)

isLeft = True

for n in range(0, 768):
  isLeft = not(isLeft)
  if (color_r < 255):
    color_r += 1
  elif (color_g < 255):
    color_g += 1
  elif (color_b < 255):
    color_b += 1
  t.pencolor((color_r, color_g, color_b))
  t.forward(50)
  if isLeft:
    t.left(179.5)
  else:
    t.right(179.5)

# keep window open
turtle.Screen().mainloop()