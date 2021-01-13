import turtle
import math
a=turtle.Turtle()
b=turtle.Turtle()
c=turtle.Turtle()
d=turtle.Turtle()
a.hideturtle()
b.hideturtle()
c.hideturtle()
d.hideturtle()
a.speed("fastest")
b.speed("fastest")
c.speed("fastest")
d.speed("fastest")
a.color("blue")
b.color("red")
c.color("yellow")
d.color("light green")
b.right(180)
c.right(90)
d.left(90)
r=5
u=5
for i in range (2000000):
    a.forward(r)
    b.forward(r)
    c.forward(r)
    d.forward(r)
    a.right(u)
    b.right(u)
    c.right(u)
    d.right(u)
    r=r+5
    u=u+5