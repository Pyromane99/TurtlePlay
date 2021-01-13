import turtle
import random
t=turtle.Turtle()
t.speed("fastest")
window=turtle.Screen()
window.bgcolor("black")
t.hideturtle()
t.color("turquoise")
for i in range(20000):
    t.forward(random.randint(25,75))
    o=random.randint(1,2)
    if o==1 :
        t.right(60)
    if o==2 :
        t.left(60)
    a=t.xcor()
    b=t.ycor()
    if a > 800 or a< -800 or b > 500 or b < -500:
        t.penup()
        t.setx(0)
        t.sety(0)
        t.pendown()
    """if i%7==0 :
        t.color("red")
    if i%11==0 :
        t.color("magenta")
    if i%13==0 :
        t.color("light green")
    if i%3==0 :
        t.color("white")
    if i%4==0 :
        t.color("yellow")
    if i%5==0 :
        t.color("blue")"""
    
    