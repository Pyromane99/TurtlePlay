import turtle
import random
window=turtle.Screen()
window.bgcolor("black")
t=turtle.Turtle()
t.speed("fastest")
t.pensize(10)
t.color("black")
t.hideturtle()
t.penup()
t.setx(400)
t.sety(200)
t.pendown()
t.right(90)
t.forward(400)
t.right(90)
t.forward(800)
t.right(90)
t.forward(400)
t.right(90)
t.forward(800)
a=turtle.Turtle()
a.color("red")
a.pensize(3)
a.speed("fastest")
a.hideturtle()
a.penup()
a.setx(random.randint(-400,400))
a.sety(random.randint(-200,200))
a.pendown()
a.setheading(random.randint(0,360))
a.forward(10)
z=0
while z!=4 :
    a.forward(5)
    x=a.xcor()
    y=a.ycor()
    if x >= 390 or x<= -390 :
        a.setheading(180-a.heading())
    if y >=190 or y<=-190 :
        a.setheading(360-a.heading())
    

    
        