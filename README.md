# Turtle Examples Using Loops
This project shows the use of loops to create simple patterns in Turtle.

## Examples

### Circles
 Rings
```python
import turtle

t = turtle.Turtle()
t.speed("fastest")

for n in range(0, 5): # number of circles
  for i in range(0, 72):    # iterations per circle
    t.forward(5)  # length to draw by
    t.right(5)  # rotate by 5 degrees
  t.forward(10) # move to next circle
```
![Rings](/Screenshots/rings.png)


------------

 Donut
 ```python
 import turtle

t = turtle.Turtle()
t.speed("fastest")

for n in range(0, 36):  # number of circles
  for i in range(0, 36):    # iterations for drawing one circle
    t.forward(3)
    t.left(10)
  t.forward(6)
  t.left(10)
  t.forward(6)
 ```
![Donut](/Screenshots/donut.png)
