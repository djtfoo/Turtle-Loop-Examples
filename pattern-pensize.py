import turtle

t = turtle.Turtle()
t.pencolor("red")
t.speed("fastest")
t.left(45)

for n in range(0, 4):
    for i in range(0, 18):
        i = 180 - i * 10
        pensize = 1
        for x in range(0, 18):
            pensize += 0.5
            t.pensize(pensize)
            t.forward(2)
            t.left(5)
        
        t.right(i)


# keep window open
turtle.Screen().mainloop()