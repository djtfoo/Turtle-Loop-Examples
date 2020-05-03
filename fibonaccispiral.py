import turtle

# turtle window
wn = turtle.Screen()
wn.setup(1920, 1080)
wn.bgcolor("orange")
wn.title("Python Turtle Graphics - Fibonacci Spiral")

# create drawer turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed("fastest")
t.right(90)
t.penup()
t.goto(250, -150)
t.pendown()

fibonacci1 = 0
fibonacci2 = 1

for n in range(0, 16): # number of fibonacci iterations
  # draw one spiral
  for i in range(0, 90):  # 90 degrees
    t.left(1)
    t.forward(fibonacci2*0.01)
  
  old = fibonacci2
  fibonacci2 = fibonacci1 + fibonacci2
  fibonacci1 = old

# keep window open
wn.mainloop()